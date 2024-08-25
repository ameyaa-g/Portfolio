# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 3
# Date:         07 08 2023

import math

side = input("Please enter the side length:")
side = float(side)


# The area of an equilateral triangle
def triarea(length):
    area = (math.sqrt(3) / 4) * length ** 2
    print("A triangle with side", "{:.2f}".format(side), "has area", "{:.3f}".format(area))

# The area of a square
def sqarea(length):
    area = (length ** 2)
    print("A square with side", "{:.2f}".format(side), "has area", "{:.3f}".format(area))


# The area of a regular pentagon
def pentarea(length):
    area = (1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * length ** 2)
    print("A pentagon with side", "{:.2f}".format(side), "has area", "{:.3f}".format(area))


# The area of a regular dodecagon (12 sides)
def dodecaarea(length):
    area = (3 * (2 + math.sqrt(3)) * length ** 2)
    print("A dodecagon with side", "{:.2f}".format(side), "has area", "{:.3f}".format(area))

# running the functions
triarea(side)
sqarea(side)
pentarea(side)
dodecaarea(side)