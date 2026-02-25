from mobilerobotics.basic import Frame
from mobilerobotics.carts import MobileCart
from mobilerobotics.visualization.mechviz import *
from sympy.physics.vector import Point
import sympy as smp
from sympy.physics.vector import ReferenceFrame, Point
from sympy import Matrix
from scipy.spatial.transform import Rotation

class TransBot_3DViz(MechaViz3D):
    def plot_mechanism(self, mech: Mechanism, scene_frame, plotter):
        MechaViz3D.plot_mechanism(self, mech, scene_frame, plotter)

        if 'transport_surface' in self.mech.extra_features:
            ts = self.mech.extra_features['transport_surface']
            centroid_pos = list(symbolic_to_numeric(ts['centroid'].pos_from(scene_frame).to_matrix(scene_frame), self.symbolic_subs)[0])
            centroid = pv.Sphere(radius=0.1, center=centroid_pos)
            plotter.add_mesh(centroid, color='yellow')
            normal = smp.matrix2numpy(symbolic_to_numeric(ts['normal'].to_matrix(scene_frame), self.symbolic_subs)[0], dtype=np.float64)
            plane = pv.Plane(center=centroid_pos, direction=normal.T)
            plotter.add_mesh(plane, color='yellow', show_edges=True)

# world = Frame('world')
cart = MobileCart()
centroid = Point('ts_c')
centroid.set_pos(cart.frame, cart.frame.z*smp.Symbol('ts_c_z'))
cart.extra_features['transport_surface'] = {
    'centroid': centroid,
    'normal': cart.frame.z
}
smp.pprint(cart.frame.pose2d)

viz3d = TransBot_3DViz(cart, use_parent_frame=False)
pass