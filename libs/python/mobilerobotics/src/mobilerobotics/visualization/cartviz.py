from ..carts.mobilecart import MobileCart
import pyvista as pv
import sympy as smp
import numpy as np
#import scipy as sc
from scipy.spatial.transform import Rotation as R

import logging
logging.basicConfig(level=logging.DEBUG,
                        format="[%(asctime)s.%(msecs)03d %(filename)s->%(funcName)s():%(lineno)s]%(levelname)s: %(message)s",
                        datefmt='%Y%m%d-%H%M%S')
logger = logging.getLogger(__name__)

class CartViz3D:
    def __init__(self, cart: MobileCart, symbolic_substitutions = {}, self_plot=True):
        self.cart = cart
        self.symbolic_subs = symbolic_substitutions

        parentFrame = pv.AxesAssembly(position=(0,0,0), orientation=(0,0,0), origin=(0,0,0))

        pos = self.symbolic_to_numeric(self.cart.frame.pos_from(self.cart.parent_frame).to_matrix(self.cart.parent_frame))
        dcm = self.symbolic_to_numeric(self.cart.frame.dcm(self.cart.parent_frame).T)
        cartFrame = pv.AxesAssembly(position=pos, orientation=R.from_matrix(dcm).as_euler('xyz', degrees=True), show_labels=False)

        if self_plot:
            plotter = pv.Plotter() 
            plotter.add_actor(parentFrame)
            plotter.add_actor(cartFrame)
            plotter.show()

    def symbolic_to_numeric(self, expr):
        subs = {}
        #rng = np.random.
        for s in expr.atoms(smp.core.function.AppliedUndef): # dynamic symbols
            if not s in self.symbolic_subs:
                self.symbolic_subs[s] = (np.random.random()-0.5)*2
                logger.warning(str(s) + " not found in symbolic_subs. Defaults to -1<=" + str(s) + "=" + str(self.symbolic_subs[s]) + "<=1")
            subs[s] = self.symbolic_subs[s]
        return expr.subs(subs)

