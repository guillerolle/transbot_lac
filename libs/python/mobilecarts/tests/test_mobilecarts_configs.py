#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy as smp
from pathlib import Path
import os

TEST_DIR = Path(__file__).parent
OUTPUT_DIR = os.path.join(TEST_DIR, "output")

import logging
logging.basicConfig(level=logging.DEBUG,
                        format="[%(asctime)s.%(msecs)03d %(filename)s->%(funcName)s():%(lineno)s]%(levelname)s: %(message)s",
                        datefmt='%Y%m%d-%H%M%S')
logger = logging.getLogger(__name__)

# from ..mobilecarts import MobileCart
from ..mobilecarts.configs.diffdrives import *
from ..mobilecarts.configs.carlikes import *

def test_differentialdrive_twowheels():
    """
        Create a 2-Wheeled Differential Drive Robot
    """
    bot = DiffDrive_2Wheels(output_path_prefix=TEST_DIR)
    logger.debug("Kinematic Configuration: (" + 
                 str(bot.notation['canudas']['delta_m']) + "," + 
                 str(bot.notation['canudas']['delta_s']) + ")")
    
    assert bot.notation['canudas']['robot_type'] == '(2,0)'

def test_differentialdrive_threewheels():
    """
        Create a 3-Wheeled Differential Drive Robot
    """
    bot = DiffDrive_3Wheels(output_path_prefix=TEST_DIR)
    logger.debug("Kinematic Configuration: (" + 
                 str(bot.notation['canudas']['delta_m']) + "," + 
                 str(bot.notation['canudas']['delta_s']) + ")")
    
    assert bot.notation['canudas']['robot_type'] == '(2,0)'


def test_differentialdrive_fourwheels():
    """
        Create a 4-Wheeled Differential Drive Robot
    """
    bot = DiffDrive_4Wheels(output_path_prefix=TEST_DIR)
    logger.debug("Kinematic Configuration: (" + 
                 str(bot.notation['canudas']['delta_m']) + "," + 
                 str(bot.notation['canudas']['delta_s']) + ")")
    
    assert bot.notation['canudas']['robot_type'] == '(2,0)'

def test_carlike_twowheels():
    """
        Create a 2-Wheeled Car-Like (bicycle) Robot
    """
    bot = Bicycle(output_path_prefix=TEST_DIR)
    logger.debug("Kinematic Configuration: (" + 
                 str(bot.notation['canudas']['delta_m']) + "," + 
                 str(bot.notation['canudas']['delta_s']) + ")")
    
    assert bot.notation['canudas']['robot_type'] == '(1,1)'

