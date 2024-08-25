# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ameya Gopinath
#               Javier Dominguez
#               Leonard Montemayor
#               Guadalupe Medrano
# Section:      M02
# Assignment:   Lab 12
# Date:         11 25 2023

import matplotlib.pyplot as plt
import numpy as np
import math
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

# One equation for a parabola is given below in terms of its focal length (f): y=(1/(4f)) x^2 Write the Python code to
# plot two parabolas as lines on the same plot for the domain -2.0≤x≤2.0 for f=2 and f=6. Choose different colors for
# each line. Make the line for f=6 width of 6.0 and the line for f=2 width of 2.0.
# parabola graph
arr = np.linspace(-2.0, 2.0, 20)
f2 = []
f6 = []
for x in arr:
    y2 = (1 / (4 * 2)) * x ** 2
    y6 = (1 / (4 * 6)) * x ** 2
    f2.append(y2)
    f6.append(y6)

fig, ax = plt.subplots()
ftwo, = ax.plot(arr, f2, color= 'red')
fsix, = ax.plot(arr, f6, color= 'blue', linewidth = '5.0')
ax.title.set_text('Parabola plots with varying focal length')
ax.set_xlabel('x')
ax.set_ylabel('y')
ftwo.set_label('f=2')
fsix.set_label('f=6')
ax.legend()

# Write the Python code to plot (x,y) points for the cubic polynomial y=2x^3+3x^2-11x-6 for the domain -4.0≤x≤4.0.
# cubic graph
arr1 = np.linspace(-4.0, 4.0, 25)
out = []
for x in arr1:
    y = 2 * x ** 3 + 3 * x ** 2 - 11 * x - 6
    out.append(y)
fig1, ax1 = plt.subplots()
ax1.plot(arr1, out, '*', color = 'yellow', markeredgecolor = 'black', markersize = '10.0')
ax1.title.set_text('Plot of cubic polynomial')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# Write the Python code to plot sin⁡(x) and cos⁡(x) using two subplots with different color lines for
# the domain -2π≤x≤2π. Display a grid on both plots.
# cos and sin graph
start = -2 * math.pi
stop = 2 * math.pi
cos = []
sin = []
arr2 = np.linspace(start, stop, 60)
for x in arr2:
    y1 = math.cos(x)
    cos.append(y1)
    y2 = math.sin(x)
    sin.append(y2)
fig2, (ax2, ax3) = plt.subplots(2)
cos, = ax2.plot(arr2, cos, color='red')
sin, = ax3.plot(arr2, sin, color='grey')
ax3.set_xlabel('x')
ax2.set_ylabel('y=cos(x)')
ax3.set_ylabel('y=sin(x)')
cos.set_label('cos(x)')
sin.set_label('sin(x)')
ax3.legend(loc = 'upper right')
ax2.legend(loc = 'lower right')

plt.show()





