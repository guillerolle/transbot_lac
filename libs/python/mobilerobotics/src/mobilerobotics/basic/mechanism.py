from . import Frame
from sympy.physics.mechanics.body_base import BodyBase
from sympy.physics.mechanics.joint import Joint
from sympy.physics.vector import Point, Vector
import sympy as smp

class Box3D():
    def __init__(self, name, frame : Frame):
        #prefix = name + "_"
        self.prefix = name + "_"
        pfx = self.prefix
        self.frame = frame 
        self.center = Point(pfx + 'c')
        self.center.set_pos(frame, 0)
        self.size = smp.Matrix([smp.Symbol(pfx + 'L'),
                                smp.Symbol(pfx + 'W'),
                                smp.Symbol(pfx + 'H')])
        l = self.size[0]
        w = self.size[1]
        h = self.size[2]
        self.vertices = [
            # self.center.locatenew(pfx + '1', frame.x*l/2 + frame.y*w/2 + frame.z*h/2)
        ]

class Mechanism():
    def __init__(self, name, parent_frame = None):
        self.name = name 
        self.frame = Frame(str(name) + "_frame")
        self.parent_frame = None

        # sub: bodies, joints and mechanisms 
        self.bodies: list[BodyBase] = []
        self.joints: list[Joint] = []
        self.mechanisms: list['Mechanism'] = []

        # extra features
        self.extra_features = {
            'bounding_box': None
        }

    def add_body(self, body: BodyBase):
        self.bodies.append(body)

    def add_joint(self, joint: Joint):
        self.joints.append(joint)

    def add_mechanism(self, mechanism: 'Mechanism', position = (0,0,0)):
        mechanism.frame.set_pos(self.frame, 
                                self.frame.x*position[0]+
                                self.frame.y*position[1]+
                                self.frame.z*position[2]
                                )
        mechanism.frame.orient(self.frame, 'DCM', smp.eye(3))
        self.mechanisms.append(mechanism)



    def symbolic_to_numeric(self, expr):
        subs = {}
        #rng = np.random.
        for s in expr.atoms(smp.core.function.AppliedUndef): # dynamic symbols
            if not s in self.symbolic_subs:
                self.symbolic_subs[s] = (np.random.random()-0.5)*2
                logger.warning(str(s) + " not found in symbolic_subs. Defaults to -1<=" + str(s) + "=" + str(self.symbolic_subs[s]) + "<=1")
            subs[s] = self.symbolic_subs[s]
        return expr.subs(subs)