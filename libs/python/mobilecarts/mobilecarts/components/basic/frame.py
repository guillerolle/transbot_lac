from sympy.physics.mechanics import ReferenceFrame, Point
from sympy.physics.vector import Vector

class Frame:
    def __init__(self, name=""):
        self.frame = ReferenceFrame(name=name)
        self.origin = Point(name=name + ".O")
        self.origin.set_vel(self.frame, Vector(0))