from sympy.physics.vector import ReferenceFrame, Point
import sympy as smp
from sympy.physics.mechanics import dynamicsymbols

class Frame(ReferenceFrame, Point):
    def __init__(self, name, **kwargs):
        ReferenceFrame.__init__(self, name, **kwargs)
        Point.__init__(self, name, **kwargs)

    def locatenew(self, name, value):
        """Creates a new frame with a position defined from this frame 
        (adapted from Point.locatenew(.)).

        Parameters
        ==========

        name : str
            The name for the new frame
        value : Vector
            The position of the new frame relative to this frame

        """

        if not isinstance(name, str):
            raise TypeError('Must supply a valid name')
        p = Frame(name)
        p.set_pos(self, value)
        self.set_pos(p, -value)
        return p
        

class Frame2DConstrained(Frame):
    def __init__(self, name, otherframe, 
                 x = dynamicsymbols('x', real=True),
                 y = dynamicsymbols('y', real=True), 
                 Z = dynamicsymbols(r'\theta', real=True), 
                 **kwargs):
        Frame.__init__(self, name, **kwargs)

        self.pose2d = smp.Matrix([x,y,Z])
        self.otherframe = otherframe

        self.set_pos(otherframe, otherframe.x*x + otherframe.y*y)
        self.orient_axis(otherframe, otherframe.z, Z)