# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 5
# Date:         9 23 2023
import math

Ay = 1000
Ax = 1.3
By = 7000
Bx = 5
Cx = 30
Cy = 1.5 * 10 ** 6
Dx = 120
Dy = 2.5 * 10 ** 4
Ex = 1200
Ey = 1.5 * 10 ** 6


# Make the slope

def slope(x1, y1, x2, y2):
    ratioy = math.log10(y2/y1)
    ratiox = math.log10(x2/x1)
    s = ratioy/ratiox
    return s


def boiling(temp, x0, y0, s):
    bp = y0 * ((temp / x0) ** s)
    return bp


# Ask for excess temp:
x = float(input("Enter the excess temperature: "))

# Use if statements to figure out if the temp is negative and therefore invalid
if x < Ax:
    print("Surface heat flux is not available")
# Use elif else to check which part of the graph this temperature belongs to
elif x == Ax:
    print(f'The surface heat flux is approximately {Ay:.0f} W/m^2')
elif x == Bx:
    print(f'The surface heat flux is approximately {By:.0f} W/m^2')
elif x == Cx:
    print(f'The surface heat flux is approximately {Cy:.0f} W/m^2')
elif x == Dx:
    print(f'The surface heat flux is approximately {Dy:.0f} W/m^2')
elif x == Ex:
    print(f'The surface heat flux is approximately {Ey:.0f} W/m^2')
elif Ax < x < Bx:
    # Call the slope function
    # Use the equation of that segment to calculate the y value
    m = slope(Ax, Ay, Bx, By)
    q = boiling(x, Ax, Ay, m)
    print(f'The surface heat flux is approximately {q:.0f} W/m^2')
elif Bx < x < Cx:
    # Call the slope function
    # Use the equation of that segment to calculate the y value
    m2 = slope(Bx, By, Cx, Cy)
    q2 = boiling(x, Bx, By, m2)
    print(f'The surface heat flux is approximately {q2:.0f} W/m^2')
elif Cx < x < Dx:
    # Call the slope function
    # Use the equation of that segment to calculate the y value
    m = slope(Cx, Cy, Dx, Dy)
    q = boiling(x, Cx, Cy, m)
    print(f'The surface heat flux is approximately {q:.0f} W/m^2')
elif Dx < x < Ex:
    # Call the slope function
    # Use the equation of that segment to calculate the y value
    m = slope(Dx, Dy, Ex, Ey)
    q = boiling(x, Dx, Dy, m)
    print(f'The surface heat flux is approximately {q:.0f} W/m^2')
elif Ex < x:
    print("Surface heat flux is not available")
