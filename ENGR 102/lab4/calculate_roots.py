# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 4
# Date:         09 18 2023

import math

# input A
A = float(input("Please enter the coefficient A: "))
# input B
B = float(input("\nPlease enter the coefficient B: "))
# input C
C = float(input("\nPlease enter the coefficient C: \n"))

# calculate the denominator, which is common for all cases
denom = 2 * A
# calculate the discriminant, which will dictate how many roots there are
# and whether they're imaginary
disc = B ** 2 - 4 * A * C
# if A is 0, then you'll end up dividing by 0, so you need to set a case for that
if A == 0 and B == 0:
    print("You entered an invalid combination of coefficients!")
elif A == 0:
    x1 = -C/B
    print(f"The root is x = {x1}")
# if discriminant is greater than 0, then the output is normal
elif disc > 0:
    sqrt = math.sqrt(disc)
    x1 = (-B + sqrt)/denom
    x2 = (-B - sqrt)/denom
    print(f"The roots are x = {x1} and x = {x2}")
# if discriminant is less than 0, then the square root is imaginary
elif disc < 0:
    disc = -disc
    sqrt = math.sqrt(disc)
    fir_x = str(-B/denom)
    sec_x = str(sqrt/denom)
    x1 = fir_x + " + " + sec_x + "i"
    x2 = fir_x + " - " + sec_x + "i"
    print(f"The roots are x = {x1} and x = {x2}")
# if discriminant is equal than 0, then there is only one x value
elif disc == 0:
    sqrt = math.sqrt(disc)
    x1 = (-B + sqrt) / denom
    print(f"The root is x = {x1}")

