#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,
                        format="[%(asctime)s.%(msecs)03d %(filename)s->%(funcName)s():%(lineno)s]%(levelname)s: %(message)s",
                        datefmt='%Y%m%d-%H%M%S')
logger = logging.getLogger(__name__)

from datetime import datetime
import sympy as smp
from sympy.physics.mechanics import dynamicsymbols, msubs, Body
import json
import os

from .components.mechanical.wheels import *
from .components.basic import Frame

import trimesh

class MobileCart:
    def parse_params(self, params: dict):
        self.Nf = 0
        self.Ns = 0
        self.Nc = 0
        self.N = 0
        if "wheels" in params:
            default_wheel_class = FixedWheel  # Default Wheel Class if no type specified".vylocal
            for w in params["wheels"]:
                if "type" not in w:
                    logger.warning("No Type set for Wheel " + str(w) + ". Defaults to " + str(default_wheel_class))
                    wc = default_wheel_class
                else:
                    if w["type"] == "fixed":
                        wc = FixedWheel
                        self.Nf += 1
                    elif w["type"] == "steering":
                        wc = SteeringWheel
                        self.Ns += 1
                    elif w["type"] == "castor":
                        wc = CastorWheel
                        self.Nc += 1
                    else:
                        logger.warning("Unknown type for wheel " + str(w) + ": " + w["type"] +
                                            ". Defaults to " + str(default_wheel_class))
                        wc = default_wheel_class
                if wc not in self.wheels_by_type:
                    self.wheels_by_type[wc]: list[wc] = []

                winst = wc(
                    name=self.mathname + r".w_{" + str(len(self.wheels)) + r"}",parent=self.chassis,
                    params=(w["params"] if "params" in w else None))
                self.wheels.append(winst)
                self.wheels_by_type[wc].append(winst)
            self.N = self.Nf + self.Ns + self.Nc
                # self.add_wheel(wheelparams=(w["params"] if "params" in w else None))
        if not 'bounding_box' in params:
            self.params['bounding_box'] = {
                'X': smp.Symbol('X'),
                'Y': smp.Symbol('Y'),
                'Z': smp.Symbol('Z')
            }
        else: 
            if not 'Z' in self.params['bounding_box']: 
                self.params['bounding_box']['Z'] = self.params['bounding_box']['X']*self.params['bounding_box']['Y']

    def __init__(self, name="", mathname="", parent_frame: Frame = None, params: dict = None, compute_canudas = True, output_path_prefix = "", viz3d=False):
        if name == "":
            logger.error("Mobile Base 'name' cannot be empty")
            raise Exception("arg 'name' in MobileBase() cannot be empty")
        
        if name is None:
            name = self.__class__.__name__

        logger.debug("Creating Mobile Base with name " + name)

        self.name = name
        if mathname == "":
            logger.debug("No 'mathname' given. Defaults to name: " + self.name)
            mathname = self.name
        self.mathname = mathname

        self.outputdir = os.path.join(output_path_prefix, "output", name)
        os.makedirs(self.outputdir, exist_ok=True)

        self.info = {
            'timestamp': datetime.now().strftime(r"%Y_%m_%d-%H_%M_%S")
        }

        self.x, self.y, self.theta = dynamicsymbols(mathname + ".x " + mathname + ".y " + mathname + r".\theta", real=True)
        self.vx, self.vy, self.omega = dynamicsymbols(mathname + ".vx " + mathname + ".vy " + mathname + r".\omega", real=True)
        self.vxlocal, self.vylocal = dynamicsymbols(mathname + r".v_x^{local} " + mathname + r".v_y^{local}", real=True)

        self.h = smp.Symbol(mathname + ".h", real=True) # altura del CM (hipótesis constante)

        self.chassis = Body(name=mathname + ".chassis")
        self.parentFrame = self.set_parent_frame(parent_frame)

        self.wheels: list[Wheel] = []
        self.wheels_by_type = {
            FixedWheel: [],
            SteeringWheel: [],
            CastorWheel: [],
        }

        # self.restriction_equations = smp.zeros(0, 1)
        # self.J1 = smp.zeros(0, 3)
        # self.J2 = None
        # self.C1 = smp.zeros(0, 3)
        # self.C2 = None

        self.params = params
        if params is not None:
            self.parse_params(params)

        self.notation = {}

        ## WHEELS VELOCITIES EQUATIONS FOR BG CONSTRUCTION
        wheel_parent_restrictions = {}
        wheel_cpoint_restrictions = {}
        for w in self.wheels:
            vel_ppExpr = smp.simplify(w.parent_joint.parent_point.vel(self.parentFrame.frame).to_matrix(self.chassis.frame))
            wheel_parent_restrictions[w.name] = [smp.Eq(w.vel_ppMatrix[i], vel_ppExpr[i], evaluate = False) for i in range(w.vel_ppMatrix.rows)]
            # Calculo las velocidades del chasis en función de las velocidades locales a la rueda para reemplazar en las restricciones abajo
            vlocal_sub = smp.solve(w.vel_ppMatrix - vel_ppExpr, [self.vxlocal, self.vylocal, self.omega])
            if not self.omega in vlocal_sub:
                vlocal_sub[self.omega] = self.omega
            
            subdict = vlocal_sub
            subdict[w.phi] = 0
            if type(w) is SteeringWheel:
                subdict[w.coords[r"\beta"]] = smp.solve(w.deltaRestriction, [w.coords[r"\beta"]])[0]
            wheel_cpoint_restrictions[w.name] = smp.simplify(msubs(
                smp.trigsimp(
                    w.floor_contact_point_tangent.vel(self.parentFrame.frame)
                                         .to_matrix(self.chassis.frame)),
                subdict
                ))
            if type(w) is SteeringWheel:
                wheel_cpoint_restrictions[w.name] = smp.trigsimp(smp.rot_axis3(w.delta)*wheel_cpoint_restrictions[w.name])

        self.notation['wheel_parent_restrictions'] = wheel_parent_restrictions
        self.notation['wheel_cpoint_restrictions'] = wheel_cpoint_restrictions

        if compute_canudas:
            try:
                self.compute_canudas_constraint_matrices()
                self.compute_feedback_linearization()
            except Exception as e:
                logger.exception(e)
                pass

            with open(os.path.join(self.outputdir, 'info.json'), 'w') as f:
                json.dump(self.info, f)

            with open(os.path.join(self.outputdir, 'canudas.dict'), 'w') as f:
                logger.info('Saving "notation" dict to ' + str(f.name))
                print(self.print_dict(self.notation), file=f)
                print(self.print_dict(self.notation), file=f)

        if viz3d:
            self.construct_visualization()
            self.cart3d.show()

    def print_dict(self, dd, prefix=""):
        # outputstr = prefix
        outputstr = ""
        for key, value in dd.items():
            outputstr += prefix + "'" + str(key) + "': "
            if type(value) is (smp.BlockMatrix or smp.MatMul):
                outputstr += str(value.as_explicit()) + ",\n"
            elif type(value) is not dict:
                outputstr += str(value) + ",\n"
            else:
                outputstr += "{\n" + self.print_dict(value, prefix=prefix + "\t")
        outputstr += "}\n"
        return outputstr
    
    def compute_feedback_linearization(self):
        logger.info('Computando leyes de control segun Canudas, Cap. 8')
        self.notation['canudas']['sfl'] = {}
        self.notation['canudas']['sfl']['P'] = {}
        self.notation['canudas']['sfl']["P'"] = {}

        if self.notation['canudas']['robot_type'] == "(2,0)":
            Ppos = 0
            for wf in self.wheels_by_type[FixedWheel]:
                Ppos += wf.body.point.pos_from(self.chassis.masscenter).express(self.chassis.frame).simplify()
            Ppos = Ppos/len(self.wheels_by_type[FixedWheel])
            Ppos = Ppos.simplify()

            self.notation['canudas']['sfl']['P']['symbol'] = self.chassis.masscenter.locatenew(self.mathname + '.P', Ppos)
            self.notation['canudas']['sfl']["P'"]['symbol'] = self.notation['canudas']['sfl']['P']['symbol'].locatenew(
                self.mathname + ".P'", smp.Symbol(self.mathname + ".e") * (
                    self.chassis.frame.x*smp.cos(smp.Symbol(self.mathname + r".\delta")) + 
                    self.chassis.frame.y*smp.sin(smp.Symbol(self.mathname + r".\delta"))
                    )
                )  
        elif self.notation['canudas']['robot_type'] == "(1,1)":
            # Ppos = self.wheels_by_type[SteeringWheel][0]

            self.notation['canudas']['sfl']['P']['symbol'] = self.wheels_by_type[FixedWheel][0].body.masscenter.locatenew(self.mathname + '.P', 0)
            self.notation['canudas']['sfl']["P'"]['symbol'] = self.wheels_by_type[SteeringWheel][0].body.masscenter.locatenew(
                self.mathname + ".P'", smp.Symbol(self.mathname + ".e") * self.wheels_by_type[SteeringWheel][0].joint.parent_interframe.x
            )
        elif self.notation['canudas']['delta_m'] == 0:
            logger.warning("Delta_m es CERO. El sistema no tiene GDL -> no puede controlarse")
            return
        
        self.notation['canudas']['sfl']["P'"]['pos_from_chassis'] = self.notation['canudas']['sfl']["P'"]['symbol'].pos_from(self.chassis.masscenter).to_matrix(self.chassis.frame)
        self.notation['canudas']['sfl']["P'"]['pos_from_global'] = smp.simplify(self.notation['canudas']['sfl']["P'"]['symbol'].pos_from(self.parentFrame.origin).to_matrix(self.parentFrame.frame))
        
        self.notation['canudas']['sfl']['h'] = smp.simplify(smp.Matrix([
            [self.notation['canudas']['sfl']["P'"]['pos_from_global'][0]],
            [self.notation['canudas']['sfl']["P'"]['pos_from_global'][1]],
            ])
        )
        
    
        
        self.notation['canudas']['sfl']['dhdxi'] = smp.simplify(smp.Matrix(
            [[ 
                smp.Derivative(self.notation['canudas']['sfl']['h'][0], self.x, evaluate=True), 
                smp.Derivative(self.notation['canudas']['sfl']['h'][0], self.y, evaluate=True), 
                smp.Derivative(self.notation['canudas']['sfl']['h'][0], self.theta, evaluate=True)
            ],[
                smp.Derivative(self.notation['canudas']['sfl']['h'][1], self.x, evaluate=True), 
                smp.Derivative(self.notation['canudas']['sfl']['h'][1], self.y, evaluate=True), 
                smp.Derivative(self.notation['canudas']['sfl']['h'][1], self.theta, evaluate=True)
            ],
            ]
        ))

        self.notation['canudas']['sfl']['dhdbetas'] = smp.zeros(rows=2, cols=len(self.wheels_by_type[SteeringWheel]))
        for i in range(len(self.wheels_by_type[SteeringWheel])):
            self.notation['canudas']['sfl']['dhdbetas'][0,i] =\
                smp.Derivative(self.notation['canudas']['sfl']['h'][0], self.wheels_by_type[SteeringWheel][i].coords[r'\beta'] , evaluate=True)
            self.notation['canudas']['sfl']['dhdbetas'][1,i] =\
                smp.Derivative(self.notation['canudas']['sfl']['h'][1], self.wheels_by_type[SteeringWheel][i].coords[r'\beta'] , evaluate=True)

        self.notation['canudas']['sfl']['dhdbetas'] = smp.simplify(self.notation['canudas']['sfl']['dhdbetas'])

        ders_sub_dict = \
        {
            smp.Derivative(self.x, smp.Symbol('t')): self.vx,
            smp.Derivative(self.y, smp.Symbol('t')): self.vy,
            smp.Derivative(self.theta, smp.Symbol('t')): self.omega,
        }
        for ws in self.wheels_by_type[SteeringWheel]:
            ders_sub_dict[smp.Derivative(ws.coords[r"\beta"], smp.Symbol('t'))] =\
                ws.speeds[r"\beta"]
        

        self.notation['canudas']['sfl']['dhdt'] = smp.simplify(msubs(
            smp.Derivative(self.notation['canudas']['sfl']['h'], 
                        smp.Symbol('t'), evaluate=True), 
            ders_sub_dict
        ))

        self.notation['canudas']['sfl']['K'] = smp.Matrix(
            [[
                self.notation['canudas']['sfl']['dhdxi']*\
                smp.rot_axis3(self.theta).transpose()*\
                self.notation['canudas']['sigma'],

                self.notation['canudas']['sfl']['dhdbetas']
            ]]
        )
        self.notation['canudas']['sfl']['K^-1'] = smp.simplify(smp.trigsimp(
            self.notation['canudas']['sfl']['K'].inv()
        ))
        True

    def construct_visualization(self):
        self.cart3d = trimesh.Scene(base_frame=self.name+str("_baseframe"))

        bbox = self.params['bounding_box']
        self.bounding_mesh = trimesh.creation.box((bbox['X'], bbox['Y'], bbox['Z']), transform=[[1, 0, 0, 0],
                                                                                                [0, 1, 0, 0],
                                                                                                [0, 0, 1, bbox['Z']/2],
                                                                                                [0, 0, 0, 1]])
        
        self.cart3d.add_geometry(self.bounding_mesh)
        for wf in self.wheels_by_type[FixedWheel]:
            wfpos = wf.body.point.pos_from(self.chassis.masscenter).to_matrix(self.chassis.frame).simplify() 
            wfrad = wf.params['r']
            cylmesh = trimesh.primitives.Cylinder(wfrad, wfrad*0.25, transform=[[1, 0, 0, wfpos[0]],
                                                                                [0, 0, -1, wfpos[1]],
                                                                                [0, 1, 0, wfpos[2]+wfrad],
                                                                                [0, 0, 0, 1]]
                                                
            )
            self.cart3d.add_geometry(cylmesh)
        #self.scene.add_geometry((self.bounding_mesh, self.cart3d))


    def set_parent_frame(self, parent_frame: Frame):
        if parent_frame is None:
            logger.warning("No 'parent_frame' given. Defaults to 'Frame('IF')'")
            parent_frame = Frame('IF')
            self.parent_frame = parent_frame

        self.chassis.frame.orient(parent_frame.frame, 'Axis', (self.theta, parent_frame.frame.z))
        self.chassis.frame.set_ang_vel(parent_frame.frame, self.omega * parent_frame.frame.z)
        self.chassis.masscenter.set_pos(parent_frame.origin,
                                        self.x * parent_frame.frame.x +
                                        self.y * parent_frame.frame.y +
                                        self.h * parent_frame.frame.z )

        self.chassis.masscenter.set_vel(parent_frame.frame,
                                        self.vxlocal * self.chassis.frame.x +
                                        self.vylocal * self.chassis.frame.y)
        # self.chassis.masscenter.set_vel(parent_frame.frame,
        #                                 self.vx * parent_frame.frame.x +
        #                                 self.vy * parent_frame.frame.y)
        return parent_frame

    def add_wheel(self, wheelparams: dict = None):
        self.wheels.append(
            FixedWheel(name=self.name + "/W" + str(len(self.wheels)), parent=self.chassis, params=wheelparams))
        return

    def get_wheel_contactpoint_pos_global(self, wheel_id: int):
        return smp.trigsimp(self.wheels[wheel_id].floor_contact_point.pos_from(self.parentFrame.origin)
                            .to_matrix(self.parentFrame.frame))

    def get_wheel_contactpoint_vel_chassis(self, wheel_id: int):
        return msubs(smp.trigsimp(self.wheels[wheel_id].floor_contact_point_tangent.vel(self.chassis.frame)
                                  .to_matrix(self.chassis.frame)),
                     {self.wheels[wheel_id].phi: 0})

    def get_wheel_contactpoint_vel_global_atwheelframe(self, w: Wheel):
        return msubs(
            smp.trigsimp(
                w.floor_contact_point_tangent.vel(self.parentFrame.frame)
                .to_matrix(w.wheelhub_frame)),
            {
                w.phi: 0}
            )
    
    def get_wheel_contactpoint_vel_global_atwheelcontactframe(self, w: Wheel):
        return msubs(
            smp.trigsimp(
                w.floor_contact_point_tangent.vel(self.parentFrame.frame)
                .to_matrix(w.floor_contact_frame)),
            {
                w.phi: 0}
            )

    def compute_canudas_constraint_matrices(self):
        """ BASADO EN:
        de Wit, C. C., Siciliano, B., & Bastin, G. (Eds.). (1996).
            Theory of Robot Control. Springer London.
            https://doi.org/10.1007/978-1-4471-1501-4
            cap 7.2: Restrictions on robot mobility, p.270
        """
        try:
            canudas = {}
            canudas['posture_coords'] = {
                'symbol': dynamicsymbols('xi'),
                'value': smp.Matrix([self.x, self.y, self.theta])
            }
            canudas['posture_speeds'] = {
                'symbol': dynamicsymbols('\\dot{xi}'),
                'value': smp.Matrix([self.vx, self.vy, self.omega])
            }

            phif = smp.zeros(0, 1)
            phis = smp.zeros(0, 1)
            phic = smp.zeros(0, 1)
            phisw = smp.zeros(0, 1)
            betas = smp.zeros(0, 1)
            betac = smp.zeros(0, 1)

            phiact_index = 0 # CURRENT INDEX OF PHI_ACTUATED FOR COMPUTING P MATRIX
            phiact_list = [] # PHI_ACTUATED LIST

            betacact_index = 0 # CURRENT INDEX OF BETAC_ACTUATED FOR COMPUTING P MATRIX
            betacact_list = [] # BETAC_ACTUATED LIST
            
            if FixedWheel in self.wheels_by_type:
                for wf in self.wheels_by_type[FixedWheel]:
                    if phif.rows == 0:
                        phif = phif.row_insert(phif.rows, [wf.phi])
                    else:
                        phif = phif.row_insert(phif.rows, smp.Matrix([wf.phi]))
                    if wf.params['phi_actuated'] == True:
                        phiact_list.append(phiact_index)
                    phiact_index += 1
                    # betacact_index += 1


            if SteeringWheel in self.wheels_by_type:
                for ws in self.wheels_by_type[SteeringWheel]:
                    if phis.rows == 0:
                        phis = phis.row_insert(phis.rows, [ws.phi])
                    else:
                        phis = phis.row_insert(phis.rows, smp.Matrix([ws.phi]))

                    if betas.rows == 0:
                        betas = betas.row_insert(betas.rows, [ws.coords[r'\beta']])
                    else:
                        betas = betas.row_insert(betas.rows, smp.Matrix([ws.coords[r'\beta']]))

                    if ws.params['phi_actuated'] == True:
                        phiact_list.append(phiact_index)
                    phiact_index += 1
                    # betacact_index += 1

            if CastorWheel in self.wheels_by_type:
                for wc in self.wheels_by_type[CastorWheel]:
                    if phic.rows == 0:
                        phic = phic.row_insert(phic.rows, [wc.phi])
                    else:
                        phic = phic.row_insert(phic.rows, smp.Matrix([wc.phi]))

                    if betac.rows == 0:
                        betac = betac.row_insert(betac.rows, [wc.coords['beta']])
                    else:
                        betac = betac.row_insert(betac.rows, smp.Matrix([wc.coords['beta']]))

                    if wc.params['phi_actuated'] == True:
                        phiact_list.append(phiact_index)
                    if wc.params['beta_actuated'] == True:
                        betacact_list.append(betacact_index)
                    phiact_index += 1
                    betacact_index += 1
            self.Nm = len(phiact_list) + len(betacact_list)
            # betas = smp.Matrix(betas)
            # betac = smp.Matrix(betac)
            canudas['orientation_coords'] = {
                'symbol': dynamicsymbols('beta'),
                'value': smp.BlockMatrix([[betas], [betac]]),
                'betas': betas,
                'betac': betac,
            }

            canudas['rotation_coords'] = {
                'symbol': dynamicsymbols('phi'),
                'value': smp.BlockMatrix([[phif], [phis], [phic], [phisw]])
            }

            canudas['configuration_coords'] = {
                'value': smp.BlockMatrix([[canudas['posture_coords']['value']],
                                          [canudas['orientation_coords']['value']],
                                          [canudas['rotation_coords']['value']],
                                          ])
            }

            xi = canudas['posture_coords']['value']
            xid = canudas['posture_speeds']['value']
            xidlocal = smp.Matrix([self.vxlocal, self.vylocal, self.omega])

            canudas['restrictions'] = {
                'equations': smp.zeros(0, 1),
                'J1': smp.zeros(0, 3),
                'J1f': smp.zeros(0, 3),
                'J1s': smp.zeros(0, 3),
                'J1c': smp.zeros(0, 3),
                'J1sw': smp.zeros(0, 3),
                'J2': smp.zeros(0, 1),
                'C1': smp.zeros(0, 1),
                'C1f': smp.zeros(0, 3),
                'C1s': smp.zeros(0, 3),
                'C1c': smp.zeros(0, 3),
                'C2': smp.zeros(0, 1),
                'C2c': smp.zeros(0, 1),
            }

            j2list = []
            c2clist = []
            for i, w in enumerate(self.wheels_by_type[FixedWheel]):
                f = self.get_wheel_contactpoint_vel_global_atwheelframe(w)
                f = smp.Matrix([f[0], f[2]])
                m = smp.linear_eq_to_matrix(f, xidlocal.T.tolist()[0])[0]
                canudas['restrictions']['J1f'] = canudas['restrictions']['J1f'].col_join(m[0, :])
                canudas['restrictions']['C1f'] = canudas['restrictions']['C1f'].col_join(m[1, :])
                j2list.append(smp.linear_eq_to_matrix(f[0], w.phid)[0])
                canudas['restrictions']['equations'] = canudas['restrictions']['equations'].col_join(f)

            for i, w in enumerate(self.wheels_by_type[SteeringWheel]):
                f = self.get_wheel_contactpoint_vel_global_atwheelframe(w)
                f = smp.Matrix([f[0], f[2]])
                m = smp.linear_eq_to_matrix(f, xidlocal.T.tolist()[0])[0]
                canudas['restrictions']['J1s'] = canudas['restrictions']['J1s'].col_join(m[0, :])
                canudas['restrictions']['C1s'] = canudas['restrictions']['C1s'].col_join(m[1, :])
                j2list.append(smp.linear_eq_to_matrix(f[0], w.phid)[0])
                canudas['restrictions']['equations'] = canudas['restrictions']['equations'].col_join(f)

            for i, w in enumerate(self.wheels_by_type[CastorWheel]):
                f = self.get_wheel_contactpoint_vel_global_atwheelframe(w)
                f = smp.Matrix([f[0], f[2]])
                m = smp.linear_eq_to_matrix(f, xidlocal.T.tolist()[0])[0]
                canudas['restrictions']['J1c'] = canudas['restrictions']['J1c'].col_join(m[0, :])
                canudas['restrictions']['C1c'] = canudas['restrictions']['C1c'].col_join(m[1, :])
                j2list.append(smp.linear_eq_to_matrix(f[0], w.phid)[0])
                # canudas['restrictions']['C2c'] = canudas['restrictions']['C2c'].col_join(
                #     smp.linear_eq_to_matrix(f[1], w.speeds['beta'])[0]
                # )
                c2clist.append(smp.linear_eq_to_matrix(f[1], w.speeds['beta'])[0])
                canudas['restrictions']['equations'] = canudas['restrictions']['equations'].col_join(f)

            canudas['restrictions']['equations.T'] = canudas['restrictions']['equations'].T

            canudas['restrictions']['J1'] = smp.BlockMatrix(
                [
                    [canudas['restrictions']['J1f']],
                    [canudas['restrictions']['J1s']],
                    [canudas['restrictions']['J1c']],
                    [canudas['restrictions']['J1sw']],
                ]
            )
            canudas['restrictions']['J2'] = smp.Matrix.diag(j2list)
            canudas['restrictions']['C1'] = smp.BlockMatrix(
                [
                    [canudas['restrictions']['C1f']],
                    [canudas['restrictions']['C1s']],
                    [canudas['restrictions']['C1c']],
                ]
            )

            # REFERENCIA LIBRO: C1* DEFINIDO EN EQ(7.14), P.271
            canudas['restrictions']['C1*'] = smp.BlockMatrix(
                [
                    [canudas['restrictions']['C1f']],
                    [canudas['restrictions']['C1s']],
                ]
            )

            canudas['restrictions']['C2c'] = smp.Matrix.diag(c2clist)
            # canudas['restrictions']['C2'] = smp.BlockMatrix(
            #     [
            #         [smp.zeros()],
            #         [canudas['restrictions']['C1s']],
            #         [canudas['restrictions']['C1c']],
            #     ]
            # )

            self.notation['canudas'] = canudas
            self.compute_nullspace()

            self.notation['canudas']['delta_m'] = 3 - self.notation['canudas']['restrictions']['C1*'].as_explicit().rank()
            self.notation['canudas']['delta_s'] = self.notation['canudas']['restrictions']['C1s'].rank()
            self.notation['canudas']['robot_type'] = "(" + str(self.notation['canudas']['delta_m']) + "," + str(self.notation['canudas']['delta_s']) + ")"

            # self.notation['canudas']['eta'] = smp.MatrixSymbol(name='eta', n=self.notation['canudas']['sigma'].cols, m=1)
            self.notation['canudas']['eta'] = smp.Matrix(dynamicsymbols('eta_0:' +
                                                                        str(self.notation['canudas']['sigma'].cols)))
            if self.notation['canudas']['eta'].cols == 0:
                self.notation['canudas']['eta'] = smp.zeros(0, 1)
            self.notation['canudas']['zeta'] = smp.Matrix(dynamicsymbols('zeta_0:' +
                                                                         str(len(self.wheels_by_type[SteeringWheel]))))
            if self.notation['canudas']['zeta'].cols == 0:
                self.notation['canudas']['zeta'] = smp.zeros(0, 1)
            # self.notation['canudas']['zeta'] = smp.MatrixSymbol(name='zeta', n=len(self.wheels_by_type[SteeringWheel]), m=1)
            canudas = self.notation['canudas']
            xi = canudas['posture_coords']['value']
            betas = canudas['orientation_coords']['betas']
            canudas['z'] = smp.BlockMatrix([[xi], [betas]])
            canudas['B'] = smp.BlockMatrix([
                [canudas['sigma'], smp.zeros(canudas['sigma'].rows, canudas['zeta'].rows)],
                [smp.zeros(canudas['zeta'].rows, canudas['sigma'].cols), smp.eye(canudas['zeta'].rows)]
            ])
            canudas['u'] = smp.BlockMatrix([[canudas['eta']], [canudas['zeta']]])
            canudas['zdot_local'] = canudas['B'] * canudas['u']
            canudas['R'] = smp.rot_givens(0, 1, canudas['posture_coords']['value'][2], dim=2)
            RR = smp.eye(canudas['z'].rows)
            RR[0:2, 0:2] = canudas['R'].T
            canudas['RR'] = RR
            canudas['zdot'] = RR * canudas['zdot_local']

            if canudas['restrictions']['C1c'].rows != 0:
                canudas['D'] = -canudas['restrictions']['C2c']**-1*canudas['restrictions']['C1c']
            else:
                canudas['D'] = smp.zeros(0, 3)
            canudas['E'] = (-canudas['restrictions']['J2']**-1*canudas['restrictions']['J1']).as_explicit()
            try:
                logger.debug("Computando la pseudo-inversa de la matriz E. Shape: " + str(canudas['E'].shape))
                """ E_ET = canudas['E']*canudas['E'].T
                pinvEright = canudas['E'].T * E_ET.inv()
                canudas['pinv(E)_right'] = pinvEright.as_explicit().simplify() """
            except Exception as e:
                logger.warning("No se pudo calcular la pseudo-inversa por derecha de E. Error:\n\t" + str(e))
                pass

            phi = canudas['rotation_coords']['value']
            betac = canudas['orientation_coords']['betac']
            canudas['q'] = smp.BlockMatrix([
                [xi],
                [betas],
                [betac],
                [phi],
                ])
            RRR = smp.eye(canudas['q'].rows)
            RRR[0:2, 0:2] = canudas['R'].T
            Dsigma = canudas['D']*canudas['sigma']
            Esigma = canudas['E']*canudas['sigma']
            canudas['S'] = RRR * smp.BlockMatrix([
                [canudas['B']],
                [smp.BlockMatrix([Dsigma, smp.zeros(Dsigma.rows, canudas['B'].cols - Dsigma.cols)])],
                [smp.BlockMatrix([Esigma, smp.zeros(Esigma.rows, canudas['B'].cols - Esigma.cols)])],
            ])

            B_actuators = (canudas['sigma'].T*smp.BlockMatrix([canudas['D'].T, canudas['E'].T])).as_explicit()
            #P = smp.zeros(len(phiact_list), Esigma.rows)
            P = smp.zeros(self.Nc + self.N, self.Nm)
            for i, p in enumerate(betacact_list):
                P[i, p] = 1
            for i, p in enumerate(phiact_list):
                P[i+self.Nc, p+len(betacact_list)] = 1
            # Qp = smp.simplify( smp.Matrix.pinv( (P * Esigma).as_explicit() ) )

            canudas['actuators'] = {
                'phi_actuated': phiact_list,
                'B': B_actuators,
                'P': P,
                # 'Q+': Qp,
            }

            if False:
                canudas['octave_code'] = {
                    'xi': smp.octave_code(xi),
                    'betas': smp.octave_code(betas),
                    'z': smp.octave_code(canudas['z']),
                    'eta': smp.octave_code(canudas['eta']),
                    'zeta': smp.octave_code(canudas['zeta']),
                    'u': smp.octave_code(canudas['u'].as_explicit()),
                    'sigma': smp.octave_code(canudas['sigma']),
                    'pinv(sigma)_left': smp.octave_code(canudas['pinv(sigma)_left']),
                    'B': smp.octave_code(canudas['B'].as_explicit()),
                    'E': smp.octave_code(canudas['E'].as_explicit()),
                    'R': smp.octave_code(canudas['R']),
                    'RR': smp.octave_code(canudas['RR']),
                    'zdot_local': smp.octave_code(canudas['zdot_local']),
                    'S': smp.octave_code(canudas['S'].as_explicit()),
                    'q': smp.octave_code(canudas['q'].as_explicit()),
                    'requations': smp.octave_code(canudas['restrictions']['equations']).replace(";", ";\n"),
                    'Qp': smp.octave_code(canudas['actuators']['Q+']),
                    'P': smp.octave_code(canudas['actuators']['P'])
                }
    
        except Exception as e:
            raise e

    def compute_nullspace(self, subdict: dict = None):
        """
        Computes the nullspace using a subdict for parameterize configuration
        :param subdict:
        :return:
        """
        logger.debug("COMPUTING NULLSPACE FOR " + self.name)
        if subdict is None:
            subdict = {}
            # print("SYMBOLIC NULLSPACE! ATTENTION FOR ERRORS!")
        # print("WITH CONFIGURATION " + str(subdict))
        # return msubs(self.notation['canudas']['restrictions']['C1*'].as_explicit(), subdict).nullspace()
        if self.notation['canudas']['restrictions']['C1*'].as_explicit().rows != 0:
            nullbasis = smp.Matrix([self.notation['canudas']['restrictions']['C1*'].as_explicit()
                                                       .subs(subdict).nullspace()])
            if nullbasis.cols == 0:
                logger.warning("El sistema está sobre restringido! **GDL = 0**")
                nullbasis = smp.zeros(rows=3, cols=0)
                
            ## ESCALO LOS VECTORES DE LA BASE PARA EVITAR POSIBLES DIVISIONES POR CERO (P.EJ, EN CARLIKE ROBOTS) ##
            for c in range(nullbasis.cols):
                denominators = []
                for r in nullbasis[:,c]:
                    denominators.append(r.as_numer_denom()[1])
                mcm = smp.lcm(denominators) # minimo comun multiplo
                nullbasis[:,c] = smp.simplify(nullbasis[:,c]*mcm)
            
            self.notation['canudas']['sigma'] = nullbasis
        else:
            self.notation['canudas']['sigma'] = smp.eye(3)
        self.notation['canudas']['nullspace_base'] = self.notation['canudas']['sigma'].T
        try:
            sigmaT_sigma = self.notation['canudas']['sigma'].T * self.notation['canudas']['sigma']
            self.notation['canudas']['pinv(sigma)_left'] = sigmaT_sigma.inv()*self.notation['canudas']['sigma'].T
        except Exception as e:
            logger.warn("No se pudo calcular la pseudo-inversa por izquierda de sigma. Error:\n\t" + str(e))
        return
