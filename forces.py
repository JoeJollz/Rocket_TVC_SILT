# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:11:52 2026

@author: joejo
"""

import numpy as np

def thrust_direction_body(gimbal):
    
    '''
    Calcualte the unit thrust direction in body coordinates.
    
    Rotation convention:
        R = Rz(delta_z) @ Ry(delta_y)
        
    Initial thrust direction:
        [1, 0, 0]
    
    Parameters
    
    gimbal : array-like
        [delta_y, delta_z] [rad]
        
    Returns
    
    np.ndarray
        Unit thrust direction [x, y, z]
    
    '''
    
    gimbal = np.asarray(gimbal, dtype = float)
    
    if gimbal.shape !=(2,):
        raise ValueError(
            "gimbal must contain [delta_y, delta_z]"
            )
    
    if not np.all(np.isfinite(gimbal)):
        raise ValueError(
            "Gimbal angles must be finite"
            )
    
    delta_y, delta_z = gimbal
    
    cy = np.cos(delta_y)
    sy = np.sin(delta_y)
    
    cz = np.cos(delta_z)
    sz = np.sin(delta_z)
    
    direction = np.array([
        cy * cz,
        cy * sz,
        -sy
        ])
    
    return direction

def thrust_force_body(thrust, gimbal):
    
    '''
    Calculate the thrust force in body coordinates.
    
    Parameters
    
    thrust : float
        Thrust magnitude [N].
        
    gimbal : array-like
        [delta_y, delta_z] [rad]
        
    Returns
    
    np.ndarray
        Thrust force [Fx, Fy, Fz] [N].
    
    '''
    
    if not np.isfinite(thrust) or thrust < 0:
        raise ValueError(
            "Thrust must be finite and non-negative"
            )
    
    direction = thrust_direction_body(gimbal)
    
    force = thrust * direction
    
    return force

def gravity_force_inertial(mass, gravity = -9.80665):
    
    '''
    Calculate gravity force in inertial coordinates.
    
    Assumes inertial z is positive upwards.
    
    Parameters
    
    mass: float
        Rocket mass [kg]
        
    gravity : float
        Gravitational acceleration [m/s^2]
        
    Returns
    
    numpy.ndarray
        Gravity force [Fx, Fy, Fz] [N]
        
    
    '''
    
    
    if not np.isfinite(mass) or mass <=0:
        raise ValueError(
            "Mass must be finite and positive."
            )
        
    if not np.isfinite(gravity) or gravity < 0:
        raise ValueError(
            "Gravity must be finite and non-negative."
            )
        
    return np.array([
        0.0, 
        0.0,
        -mass * gravity
        ])

def thrust_moment_body(thrust_force, nozzle_position_body):
    
    ''' Calculate thrust moment about the centre of gravity.
    
    M = r x F
    
    Parameters
    
    thrust_force : array - like
        Thrust force in body coordinates [N]
        
    nozzle_position_body : array - like
        Position vector from GC to nozzle [m]
        
    Returns
    
    np.ndarray
        Moment [Mx, My, Mz] [Nm]
    
    '''
    
    
    thrust_force = np.asarray(
        thrust_force,
        dtype = float
        )
    
    nozzle_position_body = np.asarray(
        nozzle_position_body,
        dtype = float
        )
    
    if thrust_force.shape != (3,):
        raise ValueError(
            "thrust_force must have three components."
            )
    
    if nozzle_position_body.shape !=(3,):
        raise ValueError(
            "nozzle_position_body must have three components."
            )
    
    if not np.all(np.isfinite(thrust_force)):
        raise ValueError(
            "Thurst force must contain finite values."
            )
        
    if not np.all(np.isfinite(nozzle_position_body)):
        raise ValueError(
            "Nozzle position must contain finite values."
            )
    
    moment = np.cross(nozzle_position_body, 
                      thrust_force
            )
    
    return moment


def calculate_forces(
        mass,
        thrust,
        gimbal,
        nozzle_position_body,
        gravity = -9.80665
        ):

    
    thrust_force = thrust_force_body(thrust, gimbal)
    
    gravity_force = gravity_force_inertial(
        mass,
        gravity
        )
    
    thrust_moment = thrust_moment_body(
        thrust_force,
        nozzle_position_body
        )
    
    return {
        "thrust_force_body": thrust_force,
        "gravity_force_inertial": gravity_force,
        "total_moment_body": thrust_moment
        }

    
    