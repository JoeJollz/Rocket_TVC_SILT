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
            initial_gimbal = None #changed from angle to full gimbal angle. 
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
        
        if initial_gimbal is None:
            
            self.current_gimbal = np.array(
                [0.0, 0.0],
                dtype = float
                )
            
        else:
            
            self.current_gimbal = np.asarray(
                initial_gimbal,
                dtype = float
                ).copy()
            
            if self.current_gimbal.shape != (2,):
                raise ValueError(
                    "initial_gimbal must contain exactly "
                    "two values: [delta_y, delta_z]"
                    )
            
        self._validate_gimbal(self.current_gimbal)
    
    
    def _validate_gimbal(self, gimbal):
        
        if not np.all(np.isfinite(gimbal)):
            raise ValueError(
                "Gimbal position must contain finite values."
                )
        
        gimbal_magnitude = np.linalg.norm(gimbal)
        
        if gimbal_magnitude > self.max_angle:
            raise ValueError(
                "Gimbal position exceeds maximum total gimbal angle"
                )
        
    
    
    
    def update(
            self,
            commanded_gimbal,
            dt
            ):
        
        if not np.isfinite(dt) or dt <= 0:
            raise ValueError(
                "dt must be finite or greater than zero"
                )
        
        if commanded_gimbal.shape != (2,):
            raise ValueError(
                "commanded_gimbal must contain exactly two values"
                "[delta_y, delta_z]"
                )
        
        if not np.all(np.isfinite(commanded_gimbal)):
            raise ValueError(
                "Commanded gimbal position must contain finite values"
                )
        
        gimbal_error = (
            commanded_gimbal
            - self.current_gimbal
            )
        
        maximum_angle_change = (
            self.max_slew_rate * dt
            )
        
        angle_change = np.clip(
            gimbal_error,
            -maximum_angle_change,
            maximum_angle_change
            )
        
        new_gimbal = (
            self.current_gimbal + angle_change
            )
        
        gimbal_magnitude = np.linalg.norm(new_gimbal)
        
        if gimbal_magnitude > self.max_angle:
            
            new_gimbal = (
                new_gimbal *self.max_anlge / gimbal_magnitude
                )
        
        
        self.current_gimbal = new_gimbal
        
        return self.current_gimbal.copy()
    
    
        
    def reset(self, gimbal = None):
        
        if gimbal is None:
            
            gimbal = np.array(
                [0.0, 0.0],
                dtype = float
                )
        else:
            
            gimbal = np.asarray(
                gimbal, 
                dtype = float
                ).copy()
            
        if gimbal.shape !=(2,):
            raise ValueError(
                "gimbal must contain exactly two values [delta_y, delta_z]"
                )
        
        self._validate_gimbal(gimbal)
        
        self.current_gimbal = gimbal.copy()
        

        
    def get_gimbal(self):
        
        return self.current_gimbal.copy()