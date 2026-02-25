#!/bin/env python3
# -*- coding: utf-8 -*-

import stl
import numpy as np
import sys 
import argparse as ap
import pythonopenscad as posc
import subprocess as sp
import os
import solid2 as sl2 
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.join(SCRIPT_DIR, "..", "..", "..")
OPENSCAD_DIR = os.path.join(WORKSPACE_DIR, "design", "openscad")


def exportscad2stl(*args):
    def _argparse(*args):
        parser = ap.ArgumentParser(prog="openscad2physical mesh", description="Convert an OpenSCAD STL file to a physical STL file")
        parser.add_argument("input", help="The input OpenSCAD file.")
        parser.add_argument("--output", help="The output physical STL file.", default='output.stl')

        return parser.parse_args(*args)
    
    args = _argparse(*args)

    oscad_run = sp.run(["openscad", "-o", args.output, args.input])
    return args.output

def setup_argparse():
    parser = ap.ArgumentParser(description="Convert an OpenSCAD file to STL with physical properties.")
    parser.add_argument("program", help="The program to run", choices=["mesh", "physical", "all"], default="all")
    parser.add_argument('rest', nargs=ap.REMAINDER, help="Arguments to be passed to the wrapped command.")
    return parser

def main(*args):
    args = setup_argparse().parse_args(*args)
    if args.program == "mesh":
        exportscad2stl(args.rest)

if __name__ == "__main__":
    main(sys.argv[1:])