from ..basic import *
import pyvista as pv
import sympy as smp
import numpy as np
from scipy.spatial.transform import Rotation as R

import logging
logging.basicConfig(level=logging.DEBUG,
                        format="[%(asctime)s.%(msecs)03d %(filename)s->%(funcName)s():%(lineno)s]%(levelname)s: %(message)s",
                        datefmt='%Y%m%d-%H%M%S')
logger = logging.getLogger(__name__)

class MechaViz3D:
    def __init__(self, mechanism: Mechanism, symbolic_substitutions = {}, use_parent_frame = False):
        self.mech = mechanism
        self.symbolic_subs = symbolic_substitutions

        plotter = pv.Plotter()
        plotter.add_actor(pv.AxesAssembly(position=(0,0,0), orientation=(0,0,0), origin=(0,0,0)))
        
        if mechanism.parent_frame is not None and use_parent_frame:
            scene_frame = mechanism.parent_frame 
        else:
            scene_frame = mechanism.frame


        self.plot_mechanism(self.mech, scene_frame, plotter)
        # actors = self.plot_mechanism(self.mech, scene_frame)
        # for a in actors:
        #    plotter.add_actor(a)

        plotter.show()
    
    def plot_mechanism(self, mech: Mechanism, scene_frame, plotter):
        pos = symbolic_to_numeric(mech.frame.pos_from(scene_frame).to_matrix(scene_frame), self.symbolic_subs)[0]
        dcm = symbolic_to_numeric(mech.frame.dcm(scene_frame).T, self.symbolic_subs)[0]
        # actors = []
        plotter.add_actor(
            pv.AxesAssembly(
                position=pos, 
                orientation=R.from_matrix(dcm).as_euler('xyz', degrees=True), 
                show_labels=False
                )
        )

        if 'bounding_box' in mech.extra_features and mech.extra_features['bounding_box'] is not None:
            bbox: Box3D = mech.extra_features['bounding_box']
            size = symbolic_to_numeric(bbox.size, self.symbolic_subs)[0]
            center = symbolic_to_numeric(bbox.center.pos_from(scene_frame).to_matrix(scene_frame), self.symbolic_subs)[0]
            dcm = symbolic_to_numeric(bbox.frame.dcm(scene_frame).T, self.symbolic_subs)[0]
            R.from_matrix(dcm).as_euler('xyz', degrees=True)

            box = pv.Box((-size[0]/2, size[0]/2, -size[1]/2, size[1]/2, -size[2]/2, size[2]/2))
            # pv.translate(box, center=list(center))
            T = pv.Transform()\
                .rotate(smp.matrix2numpy(dcm, dtype=np.float64))\
                .translate(smp.matrix2numpy(center, dtype=np.float64)[:,0])
            box.transform(T)
            plotter.add_mesh(box, opacity=0.5, show_edges=True)


        for m in mech.mechanisms:
            self.plot_mechanism(m, scene_frame, plotter)
        # return actors
        
def symbolic_to_numeric(expr, params):
    subs = {}
    #rng = np.random.
    for s in expr.atoms(smp.core.function.AppliedUndef): # dynamic symbols
        if not s in params:
            params[s] = (np.random.random()-0.5)*2
            logger.warning(str(s) + " not found in params. Defaults to -1<=" + str(s) + "=" + str(params[s]) + "<=1")
        subs[s] = params[s]
    expr = expr.subs(subs)
    for s in expr.free_symbols:
        if not s in params:
            params[s] = np.random.random()
            logger.warning(str(s) + " not found in params. Defaults to 0<=" + str(s) + "=" + str(params[s]) + "<=1")
        subs[s] = params[s]
    return expr.subs(subs), params

