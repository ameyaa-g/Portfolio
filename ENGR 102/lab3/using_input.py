# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 3
# Date:         07 08 2023

# Calculating force with Newton's second law

import math

# Calculating force with Newton's second law
print("This program calculates the applied force given mass and acceleration")

# input the variables
mass = input("Please enter the mass (kg):")  # kg
accl = input("Please enter the acceleration (m/s^2):")  # m/s^2

# change variables from string to int and calculate
f = float(mass) * float(accl)

print("Force is", "{:.1f}".format(f), " N")


# Calculating wavelength with Bragg's second law
print("This program calculates the wavelength given distance and angle")

# input the variables
d = input("Please enter the distance (nm): ")  # nm
ang = input("Please enter the angle (degrees):")# degrees
ang = int(ang)
d = float(d)

# change variables from string to int
angle_rad = math.radians(ang)  # radians
sine = math.sin(angle_rad)  # radians

# calculations
wave_len = 2 * d * sine

print(f"Wavelength is", "{:.4f}".format(wave_len), " nm")


# Calculating Radioactive decay
print("This program calculates how much Radon-222 is left given time and initial amount")

# input the variables
time = input("Please enter the time (days):")  # days
int_amt = input("Please enter the initial amount (g):")  # grams

# change variables from string to int
time = float(time)
int_amt = float(int_amt)

# calculations
half_life = 3.8  # days
decay = int_amt * math.pow(2, (-time / half_life))
print("Radon-222 left is", "{:.2f}".format(decay), " g")


# Calculating ideal gas
print("This program calculates the pressure given moles, volume, and temperature")

# input the variables
pressure = input("Please enter the number of moles: ")  # mol
vol = input("Please enter the volume (m^3):")  # m^3
temp = input("Please enter the temperature (K):") # m^3Pa/K·mol

# change variables from string to int
pressure = float(pressure)
vol = float(vol)
temp = float(temp)

# calculations
formula = (pressure * temp * 8.314) / (vol * 1000)


print("Pressure is", "{:.0f}".format(formula), " kPa")
