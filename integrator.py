# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:37:20 2026

@author: joejo
"""

import numpy as np

from state import RocketState
from dynamics import state_derivative

def add_state_derivative(state, derivative, scale):
    
    return RocketState(
        
        position = state.position + scale * derivative["position"],
        velocity = state.velocity + scale * derivative["velocity"],
        quaternion = state.quaternion + scale * derivative["quaternion"],
        angular_velocity = (state.angular_velocity + scale * derivative["angular_velocity"])
        
        )

def rk4_step(
        state,
        rocket,
        force_body,
        moment_body,
        dt
        ):
    
    k1 = state_derivative(
        state,
        rocket,
        force_body,
        moment_body
        )
    
    state_2 = add_state_derivative(
        state,
        k1,
        dt/2
        )
    
    k2 = state_derivative(
        state_2,
        rocket,
        force_body,
        moment_body
        )
    
    
    state_3 = add_state_derivative(
        state,
        k2,
        dt/2
        )
    
    k3 = state_derivative(
        state_3,
        rocket,
        force_body,
        moment_body
        )
    
    state_4 = add_state_derivative(
        state,
        k3,
        dt)
    
    k4 = state_derivative(
        state_4,
        rocket,
        force_body,
        moment_body
        )
    
    new_state = RocketState(
        position = (
            state.position
            + dt/6
            * (
                k1["position"]
                + 2*k2["position"]
                + 2*k3["position"]
                + k4["position"]
                )
            ),
        
        velocity = (
            state.velocity
            + dt/6
            * (
                k1["velocity"]
                + 2*k2["velocity"]
                + 2*k3["velocity"]
                + k4["velocity"]
                )
            ),
        
        quaternion = (
            state.quaternion
            + dt/6
            *(
                k1["quaternion"]
                + 2*k2["quaternion"]
                + 2*k3["quaternion"]
                + k4["quaternion"]
                )
            ),
        
        angular_velocity = (
            state.angular_velocity
            + dt/6
            *(
                k1["angular_velocity"]
                + 2*k2["angular_velocity"]
                + 2*k3["angular_velocity"]
                + k4["angular_velocity"]
                )
            )
        )
    new_state.normalise_quaternion()
    
    return new_state
