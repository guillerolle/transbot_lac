#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import trimesh
import sympy as smp

L = smp.Symbol('L')

box = trimesh.primitives.Box([1,1,1], [[1,0,0,0],
                                       [0,1,0,0],
                                       [0,0,1,0],
                                       [0,0,0,1]
                            ])

boxsmall = trimesh.primitives.Box([0.4, 0.4, 0.4], 
                                  [[1,0,0,0.3],
                                   [0,1,0,0.3],
                                   [0,0,1,0.3],
                                   [0,0,0,1]]
)

difference = trimesh.boolean.difference((box, boxsmall))

scene = trimesh.Scene()

scene.add_geometry([difference, box.as_outline(), boxsmall.as_outline()])

sceneM = trimesh.Scene()
sceneM.add_geometry(scene)

scene_cpy = scene.copy()
scene_cpy.base_frame = 'sccpy'
scene_cpy.add_geometry(trimesh.primitives.Sphere(radius=0.25), parent_node_name='sccpy')

sceneM.add_geometry(scene_cpy)
sceneM.graph.update(frame_from='world', frame_to='sccpy', matrix=[[  1,0,0,0.75],
                                                                    [0,1,0,0],
                                                                    [0,0,1,0],
                                                                    [0,0,0,1]])
#print(sceneM.graph)
sceneM.show()

# difference.show()
# box.show(flags={'wireframe': True})
