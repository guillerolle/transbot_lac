#!/bin/env python3
# -*- coding: utf-8 -*-

# import openscad
from solid2 import cube, text, cylinder, set_global_fn

# set the number of faces for curved shapes á!
set_global_fn(100)

# create enclosure base
base = cube(100, 50, 20)
hole = cube(90, 40, 20).translate(5, 5, 5)
base = base - hole

# create enclosure lid
lid = cube(100, 50, 5).translate(0, 0, 0)
label = text('box').linear_extrude(height=1).translate(5, 5, 5)
lid = lid + label

# create reusable screw hole function
def screw_hole():
    head = cylinder(2.5, 2)
    body = cylinder(10, 1)
    return (head + body).mirror(0, 0, 1)

# cut out screw holes
offset = 3
lid -= screw_hole().translate(3, 3, 0.5)
lid -= screw_hole().translate(3, 47, 0.5)
lid -= screw_hole().translate(97, 3, 0.5)
lid -= screw_hole().translate(97, 47, 0.5)

base -= screw_hole().translate(3, 3, 23)
base -= screw_hole().translate(3, 47, 23)
base -= screw_hole().translate(97, 3, 23)
base -= screw_hole().translate(97, 47, 23)

# move lid into position
lid = lid.translate(0, 0, 20)

# make lid transparent
lid = lid.background()

# create model
model = base + lid

# save your model for use in OpenSCAD
model.save_as_scad()

print(model)
