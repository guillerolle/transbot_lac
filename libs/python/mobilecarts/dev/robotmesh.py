#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from mobilecarts import MobileCart

bot = MobileCart(name="bot", 
                 params={
                     'bounding_box': {
                         'X': 1,
                         'Y': 1
                         },
                        "wheels": [
                {"type": "fixed",
                "params": {
                    "l": 1,
                    "beta": 1.57,
                    "alpha": -1.57,
                    "phi_actuated": False,
                    "r": 0.2,
                }},
                {"type": "fixed",
                "params": {
                    "l": 1,
                    "beta": -1.57,
                    "alpha": 1.57,
                    "phi_actuated": False,
                    "r": 0.2,
                }},
                ]
            },
                 compute_canudas=False,
                 viz3d=True)
