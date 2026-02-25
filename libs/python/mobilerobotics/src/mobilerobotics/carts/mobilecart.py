# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG,
                        format="[%(asctime)s.%(msecs)03d %(filename)s->%(funcName)s():%(lineno)s]%(levelname)s: %(message)s",
                        datefmt='%Y%m%d-%H%M%S')
logger = logging.getLogger(__name__)

from datetime import datetime
import sympy as smp
from sympy.physics.mechanics import dynamicsymbols, msubs, RigidBody
import json
import os

from ..basic import *

class SingleChassis(Mechanism):
    def __init__(self, name = "chassis_mech", **kwargs):
        Mechanism.__init__(self, name=name)
        chassis = RigidBody("chassis", self.frame)
        self.add_body(chassis)
        

class MobileCart(Mechanism):
    def __init__(self, name = "cart", parent_frame: Frame = None, **kwargs):
        Mechanism.__init__(self, name)

        # create world for cart and constrain to 2D
        if parent_frame is None:
            self.parent_frame = Frame('world_' + str(self.name))
        else:
            self.parent_frame = parent_frame
        self.frame = Frame2DConstrained(name=name+str("_frame"), otherframe=self.parent_frame)
        ############################################
        box = Box3D(name + '_bounding_box', self.frame)
        box.size[2] = box.size[0]*box.size[1]
        box.center.set_pos(self.frame, self.frame.z*box.size[2]/2)
        self.extra_features['bounding_box'] = box

        self.add_mechanism(SingleChassis(), (0,0,smp.Symbol('h_0', real=True, positive=True)))
        

