# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:       # Names:        Ameya Gopinath
#               Javier Dominguez
 #               Leonard Montemayor
#               Guadalupe Medrano
# Section:      M02
# Assignment:   Lab 3.16
# Date:         11 09 2023

t1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))

t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

# rates of x, y, and z over time

xrate = (x2 - x1)/(t2 - t1)
yrate = (y2 - y1)/(t2 - t1)
zrate = (z2 - z1)/(t2 - t1)

# initial time

t = t1
while t <= t2:

        # time within the linear interpolation period

        t1_diff = t - t1

        # formula for multiplying rate by the time

        final1_x = xrate * t1_diff + x1
        final1_y = yrate * t1_diff + y1
        final1_z = zrate * t1_diff + z1

        print(f'\nAt time {t:.2f} seconds the object is at ({final1_x:.3f}, {final1_y:.3f}, {final1_z:.3f})')

        t += (t2 - t1)/4

