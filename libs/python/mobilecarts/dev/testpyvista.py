import pyvista as pv

# Create primitives
cube = pv.Cube().triangulate()
cylinder = pv.Cylinder(center=(0, 0, 0), direction=(0, 0, 1), radius=0.5, height=2).triangulate()

# Boolean difference
result = cube.boolean_difference(cylinder)

# Create a plotter
plotter = pv.Plotter()
plotter.add_mesh(result, style='surface', color='blue', line_width=3)
#plotter.add_mesh(cube, style='surface', color='red', opacity=0.5)
plotter.show()