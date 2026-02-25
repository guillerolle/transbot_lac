#!/bin/env python3
# -*- coding: utf-8 -*-

import json
import stl
import numpy as np
import sys 
import argparse as ap
import pythonopenscad as posc
import subprocess as sp
import os
import solid2 as sl2 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

_t = sl2.scad_inline('$t')

class Part():
    def parse_arguments(self, *args, **kwargs):
        parser = ap.ArgumentParser(prog="Assembly", description='Create an assembly')
        parser.add_argument('--name', '-n', type=str, help='Name of the assembly', default='Assembly')
        parser.add_argument('--scad', '-s', type=str, help='Path to the OpenSCAD file defining the part', default=None)
        parser.add_argument('--module', '-m', type=str, help='Name of the module in the OpenSCAD file to use as the part', default=None)
        parser.add_argument('--params', '-p', type=json.loads, nargs='*', help='List of parameters for the part', default=[])
        args, unkwowns = parser.parse_known_args(*args)
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(args, key):
                    setattr(args, key, value)
                else:
                    # Optional: warn about unknown keys
                    print(f"Warning: Ignoring unknown key '{key}' in kwargs")
        return args, unkwowns
    
    def __init__(self, stl=False, *args, **kwargs):
        args, unknowns = self.parse_arguments(*args, **kwargs)
        self.name = args.name
        self.scad = args.scad
        self.module = args.module
        self.params = args.params

        self.imp = sl2.import_scad(self.scad)
        self.mdl : sl2.OpenSCADObjectPlus = getattr(self.imp, self.module)(**self.params)

        if stl:
            self.save_as_stl()
            
        pass

    def save_as_stl(self):
        self.mdl.save_as_stl(f"{self.name}.stl")

class Joint():
    def parse_arguments(self, *args, **kwargs):
        parser = ap.ArgumentParser(prog="Assembly", description='Create an assembly')
        parser.add_argument('--name', '-n', type=str, help='Name of the assembly', default='Assembly')
        parser.add_argument('--parent', '-p', type=str, help='Parent component', default=None)
        parser.add_argument('--child', '-c', type=str, help='Child component', default=None)
        parser.add_argument('--type', '-t', type=str, help='Type of joint', default=None)
        parser.add_argument('--axis', '-a', type=str, help='Axis of rotation for continuous joints', default=None)
        args, unkwowns = parser.parse_known_args(*args)
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(args, key):
                    setattr(args, key, value)
                else:
                    # Optional: warn about unknown keys
                    print(f"Warning: Ignoring unknown key '{key}' in kwargs")
        return args, unkwowns
    
    def __init__(self, parent_assembly, stl=False, *args, **kwargs):
        args, unknowns = self.parse_arguments(*args, **kwargs)
        self.name = args.name
        self.parent = args.parent
        self.child = args.child
        self.type = args.type
        self.axis = args.axis

        if self.parent is None:
            self.parent = {
                "name": parent_assembly.name,
                "position": [0, 0, 0],
                "orientation": [0, 0, 0]
            }
        if not "name" in self.parent:
            self.parent["name"] = parent_assembly.name
        if not "position" in self.parent:
            self.parent["position"] = [0, 0, 0]
        if not "orientation" in self.parent:
            self.parent["orientation"] = [0, 0, 0]

        if not "position" in self.child:
            self.child["position"] = [0, 0, 0]
        if not "orientation" in self.child:
            self.child["orientation"] = [0, 0, 0]

        if self.axis is None and (self.type == "continuous" or self.type == "prismatic"):
            self.axis = [0, 0, 1]

        self.parent_assembly = parent_assembly
        
        self.parent_component = parent_assembly.get_component_by_name(self.parent["name"])
        self.child_component = parent_assembly.get_component_by_name(self.child["name"])

        # self.mdl = self.get_mdl()

    def get_mdl(self):
        match self.type:
            case "fixed":
                mdl = self.child_component.mdl if self.child_component is not None else None
                for j in self.parent_assembly.get_children_joints(self.name):
                    if mdl is None:
                        mdl = j.get_mdl()
                    else:
                        mdl += j.get_mdl()

                return mdl.rotate(self.child['orientation']).translate(self.child['position'])\
                    .rotate(self.parent['orientation']).translate(self.parent['position'])
            case "continuous":
                mdl = self.child_component.mdl if self.child_component is not None else None
                for j in self.parent_assembly.get_children_joints(self.name):
                    if mdl is None:
                        mdl = j.get_mdl()
                    else:
                        mdl += j.get_mdl()

                return mdl.rotate(self.child['orientation']).translate(self.child['position'])\
                    .rotate(_t*360, self.axis)\
                    .rotate(self.parent['orientation']).translate(self.parent['position'])


class Assembly():    
    def parse_arguments(self, *args, **kwargs):
        parser = ap.ArgumentParser(prog="Assembly", description='Create an assembly')
        parser.add_argument('--name', '-n', type=str, help='Name of the assembly', default='Assembly')
        parser.add_argument('--components', '-c', type=json.loads, nargs='*', help='List of components to include in the assembly', default=[])
        parser.add_argument('--joints', '-j', type=json.loads, nargs='*', help='List of joints to include in the assembly', default=[])
        parser.add_argument('--assy', '-a', type=str, nargs='*', help='Sub-assembly file', default=None)

        args, unkwowns = parser.parse_known_args(*args)
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(args, key):
                    setattr(args, key, value)
                else:
                    # Optional: warn about unknown keys
                    print(f"Warning: Ignoring unknown key '{key}' in kwargs")
        return args, unkwowns
    
    def __init__(self, parent_assembly=None, *args, **kwargs):
        args, unknowns = self.parse_arguments(*args, **kwargs)


        self.name = args.name
        self.components = self.load_components(args.components)
        self.joints = self.load_joints(args.joints) 
        self.parent_assembly = parent_assembly

        self.mdl = self.get_mdl()
        if parent_assembly is None:
            self.mdl.save_as_scad(f"{self.name}.scad")
        pass

    def get_mdl(self):
        mdl = None 
        for j in self.joints:
            if j.parent["name"] == self.name:
                if mdl is None:
                    mdl = j.get_mdl()
                else:
                    mdl += j.get_mdl()
        return mdl

    def load_components(self, components) -> list:
        result = []
        for c in components:
            logger.debug(f"Loading component: {c}")
            if 'scad' in c:
                result.append(Part(**c, stl=True))
            if 'assy' in c:
                with open(c['assy'], 'r') as f:
                    data = json.load(f)
                    data["name"] = c['name']
                    result.append(Assembly(parent_assembly=self, **data ))
        return result
    
    def load_joints(self, joints) -> list:
        result = []
        for j in joints:
            logger.debug(f"Loading joint: {j}")
            result.append(Joint(self, **j))
        return result
    
    def get_component_by_name(self, name) -> Part:
        for c in self.components:
            if c.name == name:
                return c
        return None
    
    def get_joint_by_name(self, name) -> Joint:
        for j in self.joints:
            if j.name == name:
                return j
        return None

    def get_children_joints(self, joint_name) -> list:
        joint = self.get_joint_by_name(joint_name)
        if joint is None:
            raise ValueError(f"Joint '{joint_name}' not found in assembly '{self.name}'")
        result = []
        for j in self.joints:
            if j.parent["name"] == joint.child["name"]:
                result.append(j)
        return result
        
    


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    def parse_arguments(*args):  
        parser = ap.ArgumentParser(description='OpenSCAD Assembly')      
        parser.add_argument('--json', type=str, help='Path to the JSON file containing the assembly definition', default=None, required=False)
        # parser.add_argument('rest', nargs=ap.REMAINDER, help="Arguments to be passed to the wrapped command.")
        return parser.parse_known_args(*args)

    args, unknowns = parse_arguments(sys.argv[1:])
    if args.json:
        logger.info("Trying to load assembly from JSON file...")
        with open(args.json, 'r') as f:
            data = json.load(f)
            assembly = Assembly(**data)
    else:
        logger.info("Trying to load assembly from command line arguments...")
        assembly = Assembly(unknowns)
    print(f"Assembly name: {assembly.name}")
    print(f"Components: {assembly.components}")
    print(f"Joints: {assembly.joints}")

if __name__ == "__main__":
    main()