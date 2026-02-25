from mobilerobotics.basic import Frame
from mobilerobotics.carts import MobileCart
from mobilerobotics.visualization.cartviz import *
from sympy.physics.vector import Point
import sympy as smp
from sympy.physics.vector import ReferenceFrame, Point
from sympy import Matrix
from scipy.spatial.transform import Rotation

world = Frame('world')
cart = MobileCart(parent_frame=world)
smp.pprint(cart.frame.pose2d)
viz3d = CartViz3D(cart)
pass