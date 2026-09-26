# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:47:05 2026

@author: joejo
"""

import numpy as np

class RocketState:
    
    def __init(
            self,
            position,
            velocity,
            quaternion,
            angular_velocity
            ):
        
        self.position = np.array(position, dtype = float)
        
        self.velocity = np.array(velocity, dtype = float)
        
        self.quaternion = np.array(quaternion, dtype = float)
        
        self.angular_velocity = np.array(
            angular_velocity,
            dtype = float
            )
        
    def normalise_quaternion(self):
        
        mag = np.linalg.norm(self.quaternion)
        
        if mag == 0:
            raise ValueError("Quaternion cannot have zero magnitude")
        
        self.quaternion /= mag