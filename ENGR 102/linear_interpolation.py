# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ameya Gopinath
#               Javier Dominguez
#               Leonard Montemayor
#               Guadalupe Medrano
# Section:      M02
# Assignment:   Lab 2.8
# Date:         29 August 2023
import math

# first time measurement
t1 = 10  # minutes

# first distance measurement
dist1 = 2027  # km

# second time measurement
t2 = 10 + 45

# second distance measurement
dist2 = 23027

# rate of km per min for interpolation

rate = (dist2 - dist1)/(t2 - t1)


# formula for 25 minutes
val1 = rate * (25 - 10) + 2027

# formula for 300 minutes
val = rate * (300 - 10) + 2027

# calculating the circumference of the earth
cir_earth = 2 * math.pi * 6745

# finding how far ISS is from Houston
final = (val % cir_earth)


# printing values
print("Part 1: ")
print("For t = 25 minutes, the position p = ", val1, "kilometers")
print("Part 2: ")
print("For t = 300 minutes, the position p = ", final, "kilometers")

