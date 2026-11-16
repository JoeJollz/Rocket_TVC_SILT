# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:16 2026

@author: jrjol
"""

import numpy as np

from rocket import Rocket
from state import RocketState
from integrator import rk4_step


# ============================================================
# Create rocket
# ============================================================

rocket = Rocket(
    mass=100.0,
    length=5.0,
    diameter=0.5,
    cg_position=2.5,
    cp_position=3.0,
    Ixx=10.0,
    Iyy=20.0,
    Izz=30.0
)


initial_angular_velocity = np.array([
    1.0,
    2.0,
    3.0
])


state = RocketState(
    position=[0.0, 0.0, 0.0],
    velocity=[0.0, 0.0, 0.0],
    quaternion=[1.0, 0.0, 0.0, 0.0],
    angular_velocity=initial_angular_velocity
)

# ============================================================
# Force along BODY x-axis
# ============================================================

force_body = np.array([
    0.0,
    0.0,
    0.0
])

moment_body = np.array([
    0.0,
    0.0,
    0.0
])

omega = initial_angular_velocity

I = rocket.inertia

I_omega = I @ omega

expected_initial_acceleration = np.linalg.solve(
    I,
    -np.cross(omega, I_omega)
)


# ============================================================
# Take one very small RK4 step
# ============================================================

dt = 1e-5  # seconds

new_state = rk4_step(
    state,
    rocket,
    force_body,
    moment_body,
    dt
)


# ============================================================
# Numerical angular acceleration
# ============================================================

numerical_acceleration = (
    new_state.angular_velocity
    - state.angular_velocity
) / dt

print("Initial angular velocity:")
print(state.angular_velocity)

print("\nExpected initial angular acceleration:")
print(expected_initial_acceleration)

print("\nNumerical angular acceleration:")
print(numerical_acceleration)

print("\nAngular acceleration error:")
print(
    numerical_acceleration
    - expected_initial_acceleration
)

print("\nNew angular velocity:")
print(new_state.angular_velocity)

print("\nQuaternion:")
print(new_state.quaternion)

print("\nQuaternion magnitude:")
print(np.linalg.norm(new_state.quaternion))