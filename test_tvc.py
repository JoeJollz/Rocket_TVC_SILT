# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:35:54 2026

@author: jrjol
"""

# -*- coding: utf-8 -*-

import numpy as np

from tvc import TVC



tvc = TVC(
    max_angle=np.deg2rad(5.0),
    max_slew_rate=np.deg2rad(100.0)
)

print("Initial TVC angle:")
print(np.rad2deg(tvc.get_angle()), "degrees")


print("\nTest 1: Small command")
print("----------------------------")

commanded_angle = np.deg2rad(2.0)
dt = 0.01

actual_angle = tvc.update(
    commanded_angle,
    dt
)

print("Commanded angle:", np.rad2deg(commanded_angle), "degrees")
print("Actual angle:", np.rad2deg(actual_angle), "degrees")


print("\nTest 2: Slew-rate limit")
print("----------------------------")

tvc.reset(0.0)

commanded_angle = np.deg2rad(5.0)

for i in range(6):

    actual_angle = tvc.update(
        commanded_angle,
        dt
    )

    print(
        "Time:",
        (i + 1) * dt,
        "s | Angle:",
        np.rad2deg(actual_angle),
        "degrees"
    )


print("\nTest 3: Maximum angle limit")
print("----------------------------")

tvc.reset(0.0)

commanded_angle = np.deg2rad(20.0)

for i in range(10):

    actual_angle = tvc.update(
        commanded_angle,
        0.1
    )

    print(
        "Time:",
        (i + 1) * 0.1,
        "s | Angle:",
        np.rad2deg(actual_angle),
        "degrees"
    )


print("\nTest 4: Negative angle")
print("----------------------------")

tvc.reset(0.0)

commanded_angle = np.deg2rad(-5.0)

for i in range(6):

    actual_angle = tvc.update(
        commanded_angle,
        dt
    )

    print(
        "Time:",
        (i + 1) * dt,
        "s | Angle:",
        np.rad2deg(actual_angle),
        "degrees"
    )

print("\nTest 5: Reset")
print("----------------------------")

tvc.reset(np.deg2rad(3.0))

print(
    "Reset angle:",
    np.rad2deg(tvc.get_angle()),
    "degrees"
)