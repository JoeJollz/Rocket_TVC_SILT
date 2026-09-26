# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:32:12 2026

@author: joejo
"""
# For an axisymmetric rocket, Iyy = Izz.
# Products of inertia are assumed to be zero initially.
# These assumptions can be relaxed in the Monte Carlo model.

import numpy as np

class Rocket:
    
    def __init__(
            self,
            mass,
            length,
            diameter,
            cg_position,
            cp_position,
            Ixx,
            Iyy,
            Izz,
            Ixy = 0.0,
            Ixz = 0.0,
            Iyz = 0.0
            ):
        
        self.mass = mass
        self.length = length
        self.diameter = diameter
        
        self.cg_position = cg_position 
        self.cp_position = cp_position
        
        self.reference_area = np.pi * (diameter / 2)**2
        self.reference_length = diameter
        
        self.inertia = np.array([
            [Ixx, Ixy, Ixz],
            [Ixy, Iyy, Iyz],
            [Ixz, Iyz, Izz]
            ])
    
    def get_inertia_tensor(self):
        return self.inertia
    