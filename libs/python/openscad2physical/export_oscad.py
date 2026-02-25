#!/bin/env python3
# coding: utf-8

import os
import json
import sys
import logging
import stl
import xmltodict

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
OPENSCAD_DIR = os.path.join(WORKSPACE_DIR, "design", "openscad")

def export_scad(data):
    logger.debug("Exporting SCAD data: %s", data)

    scad_fullpath = os.path.join(OPENSCAD_DIR, data['scad']) 
    scad_path = os.path.dirname(data['scad'])
    logger.debug("SCAD path: %s", scad_path)

    EXPORT_DIR = os.path.join(OPENSCAD_DIR, "exports", "meshes", scad_path, data['name'])
    os.makedirs(EXPORT_DIR, exist_ok=True)
    logger.info(f"Top export dir is: {EXPORT_DIR}")
    oscad_params = []
    for param, value in data.get("params", {}).items():
        if type(value) is str:
            value = f"\\\"{value}\\\""
        if type(value) is bool:
            value = "true" if value else "false"
        oscad_params.append(f"-D {param}={value}")
    #oscad_params_str = "-D ".join(oscad_params)
    #logger.debug(f"OpenSCAD parameters: {oscad_params_str}")

    for c in data['components']:
        density = data.get("density", 1000) # default density in kg/m^3
        if type(c) is dict: 
            density = c.get("density", density)
            c = c["name"]
        
        logger.debug("Processing component: %s", c)

        root = "/".join(c.split("/")[:-1])
        end = c.split("/")[-1]
        if end == "*":
            end = "__all__"
        logger.debug(f"Root: {root}, End: {end}")
        _export_dir = os.path.join(EXPORT_DIR, root)
        os.makedirs(_export_dir, exist_ok=True)
        logger.debug(f"Component export dir is: {_export_dir}")
        # command_oscad_png = ["openscad", "-o", f"\"{os.path.join(_export_dir, f'{end}.png')}\"", "--viewall", "-D", f"display=\\\"{c}\\\"", f"\"{scad_fullpath}\"", "2>/dev/null"]
        # os.system(' '.join(command_oscad_png))
        stl_path = os.path.join(_export_dir, f'{end}.stl')
        command_oscad_stl = ["openscad", "-o", f"\"{os.path.join(_export_dir, f'{end}.png')}\"", "-o", f"\"{stl_path}\"", "--viewall", "-D", f"display=\\\"{c}\\\"", *oscad_params, f"\"{scad_fullpath}\"", "2>&1", "|",
                             "grep", "\"ECHO: \\[\\\"joint\"", ">", f"\"{os.path.join(_export_dir, f'{end}-joints.txt')}\""]
        logger.debug(f"Running command: {' '.join(command_oscad_stl)}")
        os.system(' '.join(command_oscad_stl))

        if os.path.exists(stl_path):
            logger.info(f"Successfully exported STL for component '{c}' to '{stl_path}'")
            mesh = stl.mesh.Mesh.from_file(stl_path) 
            mesh.vectors *= 1e-3 # from mm to m 
            volume, mass, com, inertia = mesh.get_mass_properties_with_density(density)
            inertial_dict = {
                'inertial_computation': {
                    "density": density,
                    "volume": volume,
                    "inertial": {
                        "origin": {
                            "@xyz": " ".join(map(str, com)),
                            "@rpy": "0.0 0.0 0.0",
                        },
                        "mass": {
                            "@value": mass
                        },
                        "inertia": {
                            "@ixx": inertia[0][0],
                            "@ixy": inertia[0][1],
                            "@ixz": inertia[0][2],
                            "@iyy": inertia[1][1],
                            "@iyz": inertia[1][2],
                            "@izz": inertia[2][2]
                        },
                    },
                    "inertia_tensor": {
                        "@matrix": inertia.tolist()
                    }
                }                
            }
            with open(os.path.join(_export_dir, f"{end}-inertial.json"), "w") as f:
                json.dump(inertial_dict, f, indent=4)

            with open(os.path.join(_export_dir, f"{end}-inertial.xml"), "w") as f:
                xmltodict.unparse(inertial_dict, f, pretty=True)

    pass

def main():
    if len(sys.argv) < 2:
        logger.error("No input file provided. Usage: export_oscad.py <input_file.json>")
        #sys.exit(1)
        file = os.path.join(SCRIPT_DIR, "rigid_forklift_wide.json")
        logger.debug("Using default file: %s", file)
    else:   
        file = sys.argv[1]

    with open(file, 'r') as f:
        data = json.load(f)
    export_scad(data)
    pass

if __name__ == "__main__":
    main()  
