# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 2
# Date:         28 08 2023

t1 = 12
x1 = 8
y1 = 6
z1 = 7

t2 = 85
x2 = -5
y2 = 30
z2 = 9

# rates of x, y, and z over time

xrate = (x2 - x1)/(t2 - t1)
yrate = (y2 - y1)/(t2 - t1)
zrate = (z2 - z1)/(t2 - t1)

# initial time

t = 30
while t <= 60:

        # time within the linear interpolation period

        t1_diff = t - 12

        # formula for multiplying rate by the time

        final1_x = xrate * t1_diff + x1
        final1_y = yrate * t1_diff + y1
        final1_z = zrate * t1_diff + z1



        print("At time", t, "seconds:")
        print("x1 =", final1_x, "m")
        print("y1 =", final1_y, "m")
        print("z1 =", final1_z, "m")
        print("----------")

        t += 7.5





# time within the linear interpolation period

t1_diff = t - 12

# formula for multiplying rate by the time

final1_x = xrate * t1_diff + x1
final1_y = yrate * t1_diff + y1
final1_z = zrate * t1_diff + z1



print("At time", t, "seconds:")
print("x1 =", final1_x, "m")
print("y1 =", final1_y, "m")
print("z1 =", final1_z, "m")
print("----------")

t += 7.5

# time within the linear interpolation period (37.5)

t1_diff = t - 12

# formula for multiplying rate by the time

final1_x = xrate * t1_diff + x1
final1_y = yrate * t1_diff + y1
final1_z = zrate * t1_diff + z1



print("At time", t, "seconds:")
print("x1 =", final1_x, "m")
print("y1 =", final1_y, "m")
print("z1 =", final1_z, "m")
print("----------")

t += 7.5

# time within the linear interpolation period (45)

t1_diff = t - 12

# formula for multiplying rate by the time

final1_x = xrate * t1_diff + x1
final1_y = yrate * t1_diff + y1
final1_z = zrate * t1_diff + z1



print("At time", t, "seconds:")
print("x1 =", final1_x, "m")
print("y1 =", final1_y, "m")
print("z1 =", final1_z, "m")
print("----------")

t += 7.5

# time within the linear interpolation period (52.5)

t1_diff = t - 12

# formula for multiplying rate by the time

final1_x = xrate * t1_diff + x1
final1_y = yrate * t1_diff + y1
final1_z = zrate * t1_diff + z1



print("At time", t, "seconds:")
print("x1 =", final1_x, "m")
print("y1 =", final1_y, "m")
print("z1 =", final1_z, "m")
print("----------")

t += 7.5

# time within the linear interpolation period (60)

t1_diff = t - 12

# formula for multiplying rate by the time

final1_x = xrate * t1_diff + x1
final1_y = yrate * t1_diff + y1
final1_z = zrate * t1_diff + z1



print("At time", t, "seconds:")
print("x1 =", final1_x, "m")
print("y1 =", final1_y, "m")
print("z1 =", final1_z, "m")
print("----------")