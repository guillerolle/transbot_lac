#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import OMPython
from OMPython import OMCSessionZMQ, ModelicaSystem

import os
import sys
from pathlib import Path

OM_PKGS_PATH = "../../../simulation/openmodelica/packages"

def load_om(dir):
    pass

if __name__=="__main__":
    # omc = OMCSessionZMQ()
    mod = ModelicaSystem(str(Path(
        OM_PKGS_PATH+"/MobileRobots/package.mo").resolve()), 
        "MobileRobots.MobileCarts.Examples.DifferentialDrive.Sandbox.SB01_DD2W_KIN"
        )
    
    print(sys.path)
    pass