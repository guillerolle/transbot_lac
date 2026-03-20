#!/bin/env python3
# coding: utf-8

from __future__  import annotations
import ast
from dataclasses import dataclass, field
import os
import json
import shutil
import sys
import logging
import numpy as np
import stl
import xmltodict

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
OPENSCAD_DIR = os.path.join(WORKSPACE_DIR, "design", "openscad")
ROSSRC_DIR = os.path.join(WORKSPACE_DIR, "robotics", "transbot-ros2ws", "src")

@dataclass
class Joint():
    type_ : str 
    parent: str 
    child: str 
    xyz: tuple 
    rpy: list 
    axis: list = field(default_factory=list)
    limits: list = field(default_factory=list)
    command_interfaces: list = field(default_factory=list)
    mimic: list = field(default_factory=list)
    spring: list = field(default_factory=list)
    damping: list = field(default_factory=list)
    friction: list = field(default_factory=list)

    def urdf_joint_block(self):
        basedict =  {
            '@name': f"j/${{prefix}}${{name}}${{suffix}}{self.child}", 
            '@type': self.type_, 
            'origin': {
                '@xyz': " ".join(map(str, np.array(self.xyz)*1e-3)),
                '@rpy': " ".join(map(str, map(lambda x: np.deg2rad(x), self.rpy)))
            },
            'parent': {
                '@link' : f"${{prefix}}${{name}}${{suffix}}{self.parent}",
            },
            'child': {
                '@link': f"${{prefix}}${{name}}${{suffix}}{self.child}",
            },
        }
        if self.mimic and self.type_ != 'fixed': 
            basedict['mimic'] = {
                '@joint': f"j/${{prefix}}${{name}}${{suffix}}{self.mimic[0]}",
                '@multiplier': str(self.mimic[1]) if len(self.mimic) > 1 else 1,
                '@offset': str(self.mimic[2]) if len(self.mimic) > 2 else 0,                
            }
            
        if self.type_ != 'fixed' and (self.damping or self.friction):
            basedict['dynamics'] = {}
            if self.damping:
                basedict['dynamics']['@damping'] = self.damping[0]
            if self.friction:
                basedict['dynamics']['@friction'] = self.friction[0]
                
        if self.type_ == 'continuous':
            basedict['axis'] = {
                '@xyz': " ".join(map(str, self.axis))
            }
        elif self.type_ == 'prismatic':
            basedict['axis'] = {
                '@xyz': " ".join(map(str, self.axis))
            }
            basedict['limit'] = {
                '@lower': str(self.limits[0]*1e-3),
                '@upper': str(self.limits[1]*1e-3),
                '@effort': str(self.limits[2]) if len(self.limits) > 2 else 1e6,
                '@velocity': str(self.limits[3]) if len(self.limits) > 3 else 1e6,
            }
        elif self.type_ == 'revolute':
            basedict['axis'] = {
                '@xyz': " ".join(map(str, self.axis))
            }
            basedict['limit'] = {
                '@lower': str(self.limits[0]),
                '@upper': str(self.limits[1]),
                '@effort': str(self.limits[2]) if len(self.limits) > 2 else 1e6,
                '@velocity': str(self.limits[3]) if len(self.limits) > 3 else 1e6,
            }
        return basedict 
    
    def urdf_ros2control_gazebo(self):
        if self.type_ == 'fixed':
            return {}
        joint =  {
            '@name': f"j/${{prefix}}${{name}}${{suffix}}{self.child}",
            'state_interface': [
                {
                    '@name': "position",
                    'param': {
                        '@name': "initial_value",
                        '#text': 0.0
                    },
                },
                {
                    '@name': "velocity",
                },
                {
                    '@name': "effort"
                }
            ],
            'command_interface': self.get_urdf_command_interfaces()
        }
        return joint 
    
    def urdf_extra_gazebo_tags(self):
        gzdict = {}
        if self.type_ != 'fixed' and self.spring:
            gzdict['dynamics'] = {
                'implicitSpringDamper': True,
                'springStiffness': self.spring[0],
                'springReference': self.spring[1] if len(self.spring) > 1 else 0.0
            }
            
        if gzdict == {}:
            return {}
        else:
            return {
                '@reference': f"j/${{prefix}}${{name}}${{suffix}}{self.child}",
                **gzdict['dynamics']
            }
    
    def get_urdf_command_interfaces(self):
        cmd_int = []
        for c in self.command_interfaces:
            cmd_int.append({
                '@name': c
            })
        if self.mimic and len(cmd_int)>0:
            logger.warning(f"joint for '{self.child}' has both mimic and command tags which are incompatible\n" + \
                f"Defaults only to mimic! Ignoring command interfaces...")
            cmd_int = []
            
        return cmd_int 


class Component():
    def __init__(self, data : dict | str, parent : Component | None = None):
        # logger.debug(f"Processing component data: {data}")
        if isinstance(data, str):
            self.type = "part"
        elif isinstance(data, dict):
            if "type" in data:
                self.type = data["type"]
            else:
                self.type = "part" # default type is "part"
        else:
            raise ValueError(f"Invalid component data: {data}")
        
        self.stl = None # path to the STL file for this component, to be assigned after exporting from OpenSCAD
        
        self._validate_type()
        self.parent = parent
        self.joints : Joint = []
        self._populate(data)

    def _populate(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "components":
                    self.children = [Component(c, parent=self) for c in value]
                else:
                    setattr(self, key, value)
        elif isinstance(data, str):
            self.name = data
        else:
            raise ValueError(f"Invalid component data: {data}")

    def find_component_in_tree_by_name(self, name) -> Component|None :
        if self.name == name:
            return self 
        else:
            if not self.type == 'assembly':
                return None 
            
            for c in self.children:
                if hasattr(c, 'replica'):
                    for r in getattr(c, 'replica'): 
                        find_result = c.find_component_in_tree_by_name(name[:-len(r)])                    
                        if find_result:
                            return c
                else:
                    find_result = c.find_component_in_tree_by_name(name)
                    if find_result:
                        return c
            return None 
        
    def get_root_component(self):
        if self.parent is None:
            return self 
        else:
            return self.parent.get_root_component()

    def _validate_type(self):
        valid_types = ["part", "assembly"]
        assert self.type in valid_types, f"Invalid component type: {self.type}. Valid types are: {valid_types}"
        
    def __repr__(self):
        return f"{self.type} {getattr(self, 'name', None)}: parent={self.parent.name if self.parent else None}, children:{len(getattr(self, 'children', []))})"
        
    def get_parent_display_list(self) -> list[str]:
        return self.parent.get_scad_display_path()[0].split("/")[:-1] if self.parent else [""]
    
    def get_base_path(self) -> str:
        return self.get_scad_display_path()[0][:-2] if self.type=="assembly" else self.get_scad_display_path()[0]

    def get_scad_display_path(self) -> list[str]:
        if self.parent:
            parent_display_path =  self.get_parent_display_list() # remove the last part of the parent assembly display path
            # if parent_display_path != "":
            if self.type == "part":
                return ["/".join([*parent_display_path, self.name])]
            elif self.type == "assembly":
                return ["/".join([*parent_display_path, self.name, "*"]),\
                        "/".join([*parent_display_path, self.name, "_"])]            # else:
        else:
            if self.type == "assembly":
                return ["*", "_"] ## IT'S ROOT COMPONENT, WHICH HAS NO DISPLAY PATH
        
        return []
    
    def iterate_tree(self, skip_self=False, func=None):
        if not skip_self:
            if func is not None:
                func(self)
            yield self
        if hasattr(self, "children"):
            for child in self.children:
                yield from child.iterate_tree(func=func)
                
    def export_stl(self, scad_file, EXPORT_DIR, oscad_params):
        """
            Export the SCAD display path to STL and PNG using OpenSCAD command line interface.
            - scad_file: the path to the SCAD file to export from
            - EXPORT_DIR: the directory to export the STL and PNG files to
            - oscad_params: a list of additional parameters to pass to the OpenSCAD command line interface (e.g. -D parameters)
        """
        logger.debug(f"Exporting SCAD component '{self.name}' from file '{scad_file}' with parameters: {oscad_params}")

        for display in self.get_scad_display_path():
            root = "/".join(display.split("/")[:-1])
            end = display.split("/")[-1]
            if end == "*":
                end = "__all__"
            # logger.debug(f"Root: {root}, End: {end}")
            _export_dir = os.path.join(EXPORT_DIR, root)
            os.makedirs(_export_dir, exist_ok=True)
            # logger.debug(f"SCAD output export dir is: {_export_dir}")
            
            stl_path = os.path.join(_export_dir, f'{end}.stl')
            _export_stl = ["-o", f"\"{stl_path}\""] 
            if self.type == "assembly" and end == "__all__":
                _export_stl = [] # skip exporting STL for the root assembly, since it may be empty and cause OpenSCAD to fail
            
            joint_path = f"{os.path.join(_export_dir, f'{end}-joints.txt')}"

            command_oscad_stl = ["openscad",\
                "-o", f"\"{os.path.join(_export_dir, f'{end}.png')}\"",\
                *_export_stl,\
                "--viewall", "-D", f"display=\\\"{display}\\\"", *oscad_params, f"\"{scad_file}\"",\
                "2>&1", "|", "grep", "\"ECHO: \\[\\\"joint\"", ">", f"\"{joint_path}\""]
            # logger.debug(f"Running command: {' '.join(command_oscad_stl)}")
            os.system(' '.join(command_oscad_stl))
            
            
            if os.path.exists(stl_path) and _export_stl:
                logger.debug(f"Successfully exported STL for component '{display}' to '{stl_path}'")
                self.assign_stl(stl_path)
            elif _export_stl:
                logger.warning(f"Failed to export STL for component '{display}' to '{stl_path}'. Maybe the geometry is empty?")
            else:
                logger.debug(f"Skipped exporting STL for component '{display}' since it's an assembly with display path '{end}'")

            if end == "__all__":
                self.parse_joints(joint_path)
                pass
                
    def parse_joints(self, joint_path):
        assert os.path.exists(joint_path)
        with open(joint_path, "r") as f:
            for line in f.readlines():
                if not line.startswith("ECHO: "):
                    continue 

                list_str = line[6:]
                try:
                    data = ast.literal_eval(list_str)
                except (SyntaxError, ValueError):
                    # Not a valid python literalwhic
                    logger.warning(f"Not a valid python literalwhic: {list_str}")
                    continue 
                
                 # Check that we have a list with at least 3 elements and first is 'joint'
                if not isinstance(data, list) or len(data) < 3 or data[0] != "joint":
                    continue 

                joint_type = data[1] 
                joint_name = data[2]
                basepath = '/'.join(joint_name.split('/')[:-1])
                if self.get_base_path()=="":
                    if not basepath=="":
                        continue 
                
                if not basepath.startswith(self.get_base_path()):
                    logger.debug(f"Skipping joint {joint_name} because not in our hierarchy level {self.get_base_path()}")
                    continue  


                suffix = basepath.removeprefix(self.get_base_path())


                if suffix == "":
                    if self.type == 'assembly':
                        parent = "_"
                    else: # if part 
                        parent = f"{self.name}"
                else:
                    suffcomp = self.find_component_in_tree_by_name(suffix.split('/')[-1])
                    if suffcomp and suffcomp.type == 'assembly' or not suffcomp:
                            continue 
                    parent = suffix.split('/')[-1]
                
                child = f"{joint_name.split('/')[-1]}"
                child_component : Component|None = self.find_component_in_tree_by_name(child)
                if child_component:
                    if child_component.type == 'assembly':
                        child = f"{child}/_"
                
                properties = {}
                for item in data[3:]:
                    if ':' in item:
                        name, value = item.split(':', 1)
                        name = name.strip() 
                        value = value.strip() 
                        # Try to interpret values as a python literal)
                        try:
                            value = ast.literal_eval(value)
                        except (SyntaxError, ValueError):
                            # Keep as string if it's not a literal
                            logger.warning(f"Keeping as string: {value}")
                            pass
                        properties[name] = value
                    else:
                        properties[item] = None 

                self.joints.append(Joint(
                    type_ = joint_type, parent = parent, child = child, **properties)
                )
                pass

                            
    def assign_stl(self, stl_path):
        if os.path.exists(stl_path):
            self.stl = stl_path
            logger.debug(f"Assigned STL path '{stl_path}' to component '{self.name}'")
        else:
            logger.warning(f"STL file '{stl_path}' does not exist. Cannot assign to component '{self.name}'")
            
    def get_density(self):
        if hasattr(self, "density"):
            return self.density
        elif self.parent:
            return self.parent.get_density()
        else:
            return 1000 # default density in kg/m^3    
        
    def compute_inertial(self):
        if self.stl is not None:
            mesh = stl.mesh.Mesh.from_file(self.stl) 
            mesh.vectors *= 1e-3 # from mm to m 
            self.density = self.get_density()
            self.volume, self.mass, self.com, self.inertia = mesh.get_mass_properties_with_density(1000) # default density in kg/m^3
            return {
                "volume": self.volume,
                "density": self.density,
                "mass": self.mass,
                "com": self.com,
                "inertia": self.inertia
            }
        else:
            logger.warning(f"No STL assigned to component '{self.name}'. Cannot compute inertial properties.")
            return None
                
    def urdf_inertial_block(self):
        if not hasattr(self, "mass"):
            logger.warning(f"Component {self.name} has no inertial properties")
            return {}
        
        return {
            'inertial': {
                '@density': str(self.density), # NOT SURE IF XACRO/URDF WILL COMPLAIN WITH THIS
                'origin': {
                    '@xyz': " ".join(map(str, self.com)),
                    '@rpy': "0 0 0",
                },
                'mass': {
                    '@value': str(self.mass),
                },
                'inertia': {
                    "@ixx": str(self.inertia[0][0]),
                    "@ixy": str(self.inertia[0][1]),
                    "@ixz": str(self.inertia[0][2]),
                    "@iyy": str(self.inertia[1][1]),
                    "@iyz": str(self.inertia[1][2]),
                    "@izz": str(self.inertia[2][2]),
                }
            }
        }
    
    def urdf_visual_block(self):
        if not self.stl:
            return {}
        
        root = self.get_root_component()
        return {
            'visual': {
                'geometry': {
                    'mesh': {
                        '@filename': f"file:$(find {root.ros_pkg_description})/meshes/{root.name}/{self.get_scad_display_path()[-1]}.stl",
                        '@scale': f"1e-3 1e-3 1e-3",
                    }
                },
                'material': {
                    '@name': "",
                    'color': {
                        '@rgba': getattr(self, 'rgba', "1 1 1 1")
                    }
                },
            },
        }    
    
    def urdf_collision_block(self):
        if not self.stl:
            return {}
        
        root = self.get_root_component()
        return {
            'collision': {
                'geometry': {
                    'mesh': {
                        '@filename': f"file:$(find {root.ros_pkg_description})/meshes/{root.name}/{self.get_scad_display_path()[-1]}.stl",
                        '@scale': f"1e-3 1e-3 1e-3",
                    }
                }
            }
        }
        
        
    def urdf_link_block(self):
        root = self.get_root_component()

        link_dict = {
            "link": {
                "@name": f"${{prefix}}${{name}}${{suffix}}{"_" if self.type == "assembly" else ""}",
                **self.urdf_inertial_block(),
                **self.urdf_visual_block(),
                **self.urdf_collision_block(),
            }
        }
        # if hasattr(self, "children"):
        #    link_dict["link"]["component"] = [child.urdf_link_block() for child in self.children]
        return link_dict
    
    def xacro_macro(self):
        macro = {
            '@name': self.name,
            '@params': f"prefix='' name='{self.name}' suffix=''",
            **self.urdf_link_block()
        }
        
        if self.type == 'assembly':
            macro['xacro:include'] = []
            macro['joint'] = []
            root = self.get_root_component()
            for c in self.children:
                if c.type == 'part':
                    macro['xacro:include'].append({
                        '@filename': f"$(find {root.ros_pkg_description})/urdf/{root.name}/{"/".join([*c.get_parent_display_list(), c.name])}.urdf.xacro",
                    })
                elif c.type == 'assembly':
                    macro['xacro:include'].append({
                        '@filename': f"$(find {root.ros_pkg_description})/urdf/{root.name}/{"/".join([*c.get_parent_display_list(), c.name, c.name])}.urdf.xacro",
                    })
                
                if hasattr(c, 'replica'):
                    macro[f'xacro:{c.name}'] = []
                    for r in c.replica:
                        macro[f'xacro:{c.name}'].append({
                            '@prefix':"${prefix}${name}${suffix}",
                            '@suffix': f"{r}{"/" if c.type=='assembly' else ""}",
                        })
                else:
                    macro[f'xacro:{c.name}'] = {
                        '@prefix':"${prefix}${name}${suffix}",
                        '@suffix': "/" if c.type=='assembly' else "",
                    }

            for j in self.joints:
                macro['joint'].append(j.urdf_joint_block())

        return {
            'robot': {
                '@xmlns:xacro': "http://www.ros.org/wiki/xacro",
                '@name': self.name,
                'xacro:macro': macro}
        }
        
    def xacro_gazebo(self):
        macro_ros2control = {
            '@name': f"{self.name}-ros2_control_gazebo",
            '@params': f"prefix='' name='{self.name}' suffix=''"
        }
        
        macro_gzreference = {
            '@name': f"{self.name}-gz_reference",
            '@params': f"prefix='' name='{self.name}' suffix=''"
        }
        
        xacro_includes = []
        if self.type == 'assembly':
            macro_ros2control['xacro:include'] = []
            macro_ros2control['joint'] = []
            macro_gzreference['xacro:include'] = []
            macro_gzreference['gazebo'] = []
            root = self.get_root_component()
            for c in self.children:     
                if c.type == 'part':
                    continue
                elif c.type == 'assembly':
                    xacro_includes.append({
                        '@filename': f"$(find {root.ros_pkg_gazebo})/urdf/{root.name}/{"/".join([*c.get_parent_display_list(), c.name, c.name])}.urdf.xacro",
                    })           
                if hasattr(c, 'replica'):
                    macro_ros2control[f'xacro:{c.name}-ros2_control_gazebo'] = []
                    for r in c.replica:
                        macro_ros2control[f'xacro:{c.name}-ros2_control_gazebo'].append({
                            '@prefix':"${prefix}${name}${suffix}",
                            '@suffix': f"{r}{"/" if c.type=='assembly' else ""}",
                        })
                        
                    macro_gzreference[f'xacro:{c.name}-gz_reference'] = []
                    for r in c.replica:
                        macro_gzreference[f'xacro:{c.name}-gz_reference'].append({
                            '@prefix':"${prefix}${name}${suffix}",
                            '@suffix': f"{r}{"/" if c.type=='assembly' else ""}",
                        })
                else:
                    macro_ros2control[f'xacro:{c.name}-ros2_control_gazebo'] = {
                        '@prefix':"${prefix}${name}${suffix}",
                        '@suffix': "/" if c.type=='assembly' else "",
                    }
                    
                    macro_gzreference[f'xacro:{c.name}-gz_reference'] = {
                        '@prefix':"${prefix}${name}${suffix}",
                        '@suffix': "/" if c.type=='assembly' else "",
                    }

            for j in self.joints:
                if j.type_ == 'fixed':
                    continue 
                macro_ros2control['joint'].append(j.urdf_ros2control_gazebo())
                
                gz_joint = j.urdf_extra_gazebo_tags()
                if len(gz_joint) > 0:
                    macro_gzreference['gazebo'].append(gz_joint)
        
        return {
            'robot': {
                '@xmlns:xacro': "http://www.ros.org/wiki/xacro",
                '@name': self.name,
                'xacro:include': xacro_includes,
                'xacro:macro': [
                    macro_ros2control,
                    macro_gzreference
                ]
            }
        }
            
    
    def xacro_all(self):
        root = self.get_root_component()
        return {
            'robot': {
                '@xmlns:xacro': "http://www.ros.org/wiki/xacro",
                '@name': self.name,
                'xacro:include': [
                    {
                        '@filename': f"$(find {root.ros_pkg_description})/urdf/{root.name}/{"/".join([*self.get_parent_display_list(), self.name])}.urdf.xacro".replace("//","/"),
                    }
                ],
                f"xacro:{self.name}": {
                    '@prefix': "",
                    '@name': "",
                }
            }
        }
        
    def xacro_gazebo_all(self):
        root = self.get_root_component()

        return {
            'robot': {
                '@xmlns:xacro': "http://www.ros.org/wiki/xacro",
                '@name': self.name,
                'xacro:arg': [
                    {
                        '@name': 'ros2_control_namespace',
                        '@default': '/transbot',
                    },
                    {
                        '@name': 'ros2_control_dict',
                        '@default': f"{root.name}/{"/".join([*self.get_parent_display_list()]).removeprefix('/')}/ros2_control.yaml"
                    }
                ],
                'xacro:include': [
                    {
                        '@filename': f"$(find {root.ros_pkg_description})/urdf/{root.name}/{"/".join([*self.get_parent_display_list(), "__all__"])}.urdf.xacro".replace("//","/"),
                    },
                    {
                        '@filename': f"$(find {getattr(root, 'ros_pkg_gazebo')})/urdf/{root.name}/{"/".join([*self.get_parent_display_list(), self.name]).removeprefix('/')}.urdf.xacro",
                    },
                ],
                'gazebo': [
                    {
                        'plugin': {
                            '@filename': 'gz_ros2_control-system',
                            '@name': 'gz_ros2_control::GazeboSimROS2ControlPlugin',
                            'parameters': f"$(find {getattr(root,'ros_pkg_gazebo')})/config/$(arg ros2_control_dict)",
                            "ros" : {
                                'namespace': "$(arg ros2_control_namespace)"
                            }
                        }
                    },
                ],
                f"xacro:{self.name}-gz_reference": {
                    '@prefix': "",
                    '@name': "",
                },
                'ros2_control': {
                    '@name': "GazeboSimSystem",
                    '@type': "system", 
                    'hardware': {
                        'plugin': "gz_ros2_control/GazeboSimSystem"
                    },
                    f"xacro:{self.name}-ros2_control_gazebo": {
                        '@prefix': "",
                        '@name': "",
                    }
                }
            }
        }
        
    
    def urdf_save(self, EXPORT_DIR, EXPORT_DIR_GZ):
        display = self.get_scad_display_path()[0]
        
        root = "/".join(display.split("/")[:-1])
        # end = display.split("/")[-1]
        # if end == "*":
        #     end = "__all__"
        _export_dir = os.path.join(EXPORT_DIR, root)
        os.makedirs(_export_dir, exist_ok=True)
        
        _export_dir_gz = os.path.join(EXPORT_DIR_GZ, root)
        os.makedirs(_export_dir_gz, exist_ok=True)
        
        with open(os.path.join(_export_dir, f"{self.name}.urdf.xacro"), "w") as f:
            xmltodict.unparse(self.xacro_macro(), f, pretty=True)
            
        with open(os.path.join(_export_dir_gz, f"{self.name}.urdf.xacro"), "w") as f:
            xmltodict.unparse(self.xacro_gazebo(), f, pretty=True)

        if self.type == 'assembly':
            with open(os.path.join(_export_dir, f"__all__.urdf.xacro"), "w") as f:
                xmltodict.unparse(self.xacro_all(), f, pretty=True)
                
            with open(os.path.join(_export_dir_gz, f"__all__.urdf.xacro"), "w") as f:
                xmltodict.unparse(self.xacro_gazebo_all(), f, pretty=True)
   
def process_export_dict(data):
    logger.debug("Exporting SCAD data: %s", data)

    scad_fullpath = os.path.join(OPENSCAD_DIR, "models", data['scad']) 
    scad_path = os.path.dirname(data['scad'])
    logger.debug("SCAD path: %s", scad_path)
    
    ros_pkg_description = data['ros_pkg_description']
    ros_pkg_gazebo = data['ros_pkg_gazebo']

    EXPORT_DIR = os.path.join(ROSSRC_DIR, ros_pkg_description, "meshes", data['name'])
    shutil.rmtree(EXPORT_DIR, True) # clear the export directory before exporting new files
    os.makedirs(EXPORT_DIR, exist_ok=True)
    logger.info(f"Meshes export dir is: {EXPORT_DIR}")
    oscad_params = []
    for param, value in data.get("params", {}).items():
        if type(value) is str:
            value = f"\\\"{value}\\\""
        if type(value) is bool:
            value = "true" if value else "false"
        oscad_params.append(f"-D {param}={value}")
    #oscad_params_str = "-D ".join(oscad_params)
    #logger.debug(f"OpenSCAD parameters: {oscad_params_str}")
    
    logger.debug(f"Creating component tree from data: {data}")
    component_root = Component(data={**data, 'type': 'assembly'})

    for c in component_root.iterate_tree():
        c.export_stl(scad_file=scad_fullpath, EXPORT_DIR=EXPORT_DIR, oscad_params=oscad_params)

    EXPORT_DIR = os.path.join(ROSSRC_DIR, ros_pkg_description, "urdf", data['name'])
    shutil.rmtree(EXPORT_DIR, True) # clear the export directory before exporting new files
    os.makedirs(EXPORT_DIR, exist_ok=True)

    EXPORT_DIR_GZ = os.path.join(ROSSRC_DIR, ros_pkg_gazebo, "urdf", data['name'])
    shutil.rmtree(EXPORT_DIR_GZ, True) # clear the export directory before exporting new files
    os.makedirs(EXPORT_DIR_GZ, exist_ok=True)
    for c in component_root.iterate_tree():
        c.compute_inertial()
        c.urdf_save(EXPORT_DIR, EXPORT_DIR_GZ)
    pass

def main():
    if len(sys.argv) < 2:
        logger.error("No input file provided. Usage: export_oscad.py <input_file.json>")
        sys.exit(1)
        # file = os.path.join(SCRIPT_DIR, "rigid_forklift_wide.json")
        # logger.debug("Using default file: %s", file)
    else:   
        file = sys.argv[1]

    with open(file, 'r') as f:
        data = json.load(f)
    data['name'] = ".".join(file.split("/")[-1].split(".")[0:-1])
    process_export_dict(data)
    pass

if __name__ == "__main__":
    main()  
