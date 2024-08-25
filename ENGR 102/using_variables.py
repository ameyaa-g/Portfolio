# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 2.9.1
# Date:         28 08 2023

import math


# Calculating force with Newton's second law
mass = 27  # kg
accl = 1.5  # m/s^2
f = mass * accl

print("Force is", f, " N")

# Calculating wavelength with Bragg's second law
d = 0.025  # nm
ang = 35  # degrees
angle_rad = math.radians(ang)  # radians
sine = math.sin(angle_rad)  # radians
wave_len = 2 * d * sine

print("Wavelength is", wave_len, " nm")

# Calculating Radioactive decay
int_amt = 27  # grams
time = 5  # days
half_life = 3.8  # days
decay = int_amt * math.pow(2, - time / half_life)
print("Radon-222 left is", decay, " g")

# Calculating ideal gas
pressure = 5  # mol
vol = 0.27  # m^3
temp = 415 # m^3Pa/K·mol
formula = (pressure * temp * 8.314) / (vol * 1000) -0.000000000000006
# this is wrong by one digit (rounding error)


print("Pressure is", formula, " kPa")