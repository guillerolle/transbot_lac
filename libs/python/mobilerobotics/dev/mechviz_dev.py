from mobilerobotics.basic import Frame
from mobilerobotics.carts import MobileCart
from mobilerobotics.visualization.mechviz import *
from sympy.physics.vector import Point
import sympy as smp
from sympy.physics.vector import ReferenceFrame, Point
from sympy import Matrix
from scipy.spatial.transform import Rotation


world = Frame('world')
cart = MobileCart(parent_frame=world)

centroid = Point('ts_c')
centroid.pos_from(cart.frame, cart.frame.z*smp.Symbol('ts_c_z'))
cart.extra_features['transport_surface'] = {
    'centroid': centroid,
    'normal_vector': cart.frame.z
}
smp.pprint(cart.frame.pose2d)
viz3d = MechaViz3D(cart)
pass