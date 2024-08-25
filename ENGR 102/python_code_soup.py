# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 2
# Date:         28 08 2023

# print 1
z = 0
x = 1
z += x
print(z)

# print 27
z = 0
y = 10
x += 1
y *= x
x += 1
x += 1
x += 1
x += 1
x += 1
y += x
z += y
print(z)

# print 102
z = 0
x = 1
y = 10
x = y
y *= x
x = 1
x += 1
y += x
z += y
print(z)

# print 10^12

x = 1
y = 10
z = 0
x = y
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
z += y
print(z)

# print 8675

x = 1
y = 10
z = 0
x = y
y *= x
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
z += y
x = 1
y = 10
x += 1
y *= x
x += 1
x += 1
x += 1
y += x
x = y
y *= x
y += x
y += x
z += y


print(z)
