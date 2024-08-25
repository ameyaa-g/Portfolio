# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ameya Gopinath
#               Javier Dominguez
#               Leonard Montemayor
#               Guadalupe Medrano
# Section:      M02
# Assignment:   Lab 6
# Date:         10 5 2023
import math
# input the numbers
side = float(input("Enter the side length in meters:"))

layers = int(input("Enter the number of layers:"))

d = 0
for i in range(1, layers + 1):
    a = i * 3 * (side ** 2)
    # calculate the current prism's SA
    curtop = ((math.sqrt(3) / 4) * i ** 2) * (side * side)
    # calculate the previous prism's SA
    prevtop = ((math.sqrt(3) / 4) * (i - 1) ** 2) * (side * side)
    # find the difference between the two
    bal = (curtop - prevtop)
    # add up and get a total
    d = a + bal + d


# print statement
print(f"You need {d:.2f} m^2 of gold foil to cover the pyramid")





