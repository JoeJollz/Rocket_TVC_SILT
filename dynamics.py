# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:54:59 2026

@author: joejo
"""

import numpy as np

def translational_acceleration(
        mass,
        force_body,
        quaternion,
        force_inertial = None
        ):
    '''
    To calculate the translational acceleration.

    Parameters
    ----------
    mass : float
        Rocket mass (kg)
        
    force_body : array
        Total force acting on the rocket (N)
        
    quaternion : array
        Attitude quaternion [q0, q1, q2, q3]
        
    force_inertial : array, optional
        Additional force already expressed in the inertial frame (N).

    Returns
    -------
    acceleration : numpy.ndarray
        Translational acceleration in the inertial frame (m/s^2)
        
    '''
    raise NotImplementedError
    
def angular_acceleration(
        inertia,
        angular_velocity,
        moment
        ):
    '''
    Angular acceleration from Euler's rigid body equation.

    Parameters
    ----------
    inertia : np.ndarray
        3x3 inertia tensor [kg m2]
    
    angular_velocity : array
        Body-frame angular velocity (rad/s).
        
    moment : array
        Total body frame momen (Nm).

    Returns
    -------
    angular_acceleration : numpy.ndarray
        Body-frame angular acceleration (rad/s^2)
    
    '''
    
    angular_velocity = np.asarray(angular_velocity, dtype = float)
    moment = np.asarray(moment, dtype = float)
    
    inertia_omega = inertia @ angular_velocity
    
    angular_acceleration = np.linalg.solve(
        inertia,
        moment - np.cross(angular_velocity, inertia_omega)
        )

    return angular_acceleration

def quaternion_to_rotation_matrix(quaternion):
    
    q0, q1, q2, q3 = quaternion
    
    rotation_matrix = np.array([
        [
         1 - 2*(q2**2 + q3**2),
         2*(q1*q2 - q0*q3),
         2*(q1*q3 + q0*q2)
        ],
        
        [
        2*(q1*q2 + q0*q3),
        1 - 2*(q1**2 + q3**2),
        2*(q2*q3 - q0*q1)
        ],
        
        [
        2*(q1*q3 - q0*q2),
        2*(q2*q3 + q0*q1),
        1 - 2*(q1**2 + q2**2)
        ]
        
        ])
    return rotation_matrix

def quaternion_derivative(quaternion, angular_velocity):
    
    q0, q1, q2, q3 = quaternion
    p, q, r = angular_velocity
    
    omega_matrix = np.array([
        [0, -p, -q, -r],
        [p, 0, r, -q],
        [q, -r, 0, p],
        [r, q, -p, 0]
        ])
    
    quaternion_dot = 0.5 * omega_matrix @ quaternion
    
    return quaternion_dot


def state_derivative(
        state,
        mass,
        force_body,
        moment_body
        ):
    
    position = state.position
    velocity = state.velocity
    quaternion = state.quaternion
    angular_velocity = state.angular_velocity
    
    position_dot = velocity
    
    rotation_matrix = quaternion_to_rotation_matrix(
        quaternion
        )
    
    force_body = np.asarray(force_body, dtype = float)
    force_inertial = rotation_matrix @ force_body
    
    quaternion_dot = quaternion_derivative(quaternion, angular_velocity)
    
    raise NotImplementedError
