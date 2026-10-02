# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:30:34 2026

@author: jrjol
"""

import numpy as np

class TVC:
    
    def __init__(
            self,
            max_angle,
            max_slew_rate,
            initial_angle = 0.0
            ):
        
        if max_angle < 0:
            raise ValueError(
                "max_angle must be non-negative."
                )
            
        if max_slew_rate < 0:
            raise ValueError(
                "max_slew_rate must be non-negative"
                )
        
        self.max_angle = float(max_angle)
        self.max_slew_rate = float(max_slew_rate)
        
        self.current_angle = float(initial_angle)
        
        self.current_angle = np.clip(
            self.current_angle,
            -self.max_angle,
            self.max_angle
            )
    
    def update(
            self,
            commanded_angle,
            dt
            ):
        
        if dt <=0:
            raise ValueError(
                "dt must be greater than zero.")
            
        commanded_angle = np.clip(
            commanded_angle,
            -self.max_angle,
            self.max_angle
            )
        
        angle_error = (
            commanded_angle
            -self.current_angle)
        
        maximum_angle_change = (
            self.max_slew_rate *dt
            )
        
        angle_change = np.clip(
            angle_error,
            -maximum_angle_change,
            maximum_angle_change
            )
        
        self.current_angle += angle_change
        
        self.current_angle = np.clip(
            self.current_angle,
            -self.max_angle,
            self.max_angle
            )
        
    def reset(self, angle = 0.0):
        
        if abs(angle) > self.max_angle:
            raise ValueError(
                "Reset angle exceeds maximum TVC angle"
                )
        
        self.current_angle = float(angle)
        
    def get_anlge(self):
        
        return self.current_angle