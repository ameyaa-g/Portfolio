# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         AMEYA GOPINATH
# Section:      M02
# Assignment:   11 LAB
# Date:         11/17/23
#

import numpy
import matplotlib.pyplot as plt

# initial array
matrix = numpy.array([[1.02, 0.095],[-0.095, 1.02]])

point = numpy.array([[0], [1]])

# loops
for i in range(250):
    point = matrix @ point
    plt.plot(point[0], point[1], '*')

# plot math graph
plt.title('Ratio')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
