# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 1.13
# Date:         21 22 2023
import math

#my guess and title
print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print("my guess is 1")

#equation and inputs
x = 1.1
print(math.sin(x-1)/(x-1))

x = 1.01
print(math.sin(x-1)/(x-1))

x = 1.001
eq3 = math.sin(x-1)/(x-1)
print(eq3)

x = 1.0001
eq4 = math.sin(x-1)/(x-1)
print(eq4)

x = 1.00001
eq7 = math.sin(x-1)/(x-1)
print(eq7)

x = 1.000001
eq8 = math.sin(x-1)/(x-1)
print(eq8)

x = 1.0000001
eq5 = math.sin(x-1)/(x-1)
print(eq5)

x = 1.00000001
eq6 = math.sin(x-1)/(x-1)
print(eq6)

print("I was close")

list = [1.1, 1.01, 1.001, 1.0001, 1.00001, 1.000001, 1.0000001, 1.00000001]

for i in list:
    print(math.sin(i-1)/(i-1))
