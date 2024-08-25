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
# Date:         11 21 2023


# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np

# A,B,C matrices

A = np.array([[0,  1,  2,  3],
 [4,  5,  6,  7],
 [8,  9, 10, 11]])
print('A = ',A)
print("")

B = np.array([[0, 1],
 [2, 3],
 [4, 5],
 [6, 7]])

print('B = ',B)
print("")

C = np.array([[0, 1, 2],
 [3, 4, 5]])


print('C = ', C)
print("")

print('D = ', A @ B @ C)
print("")

D = np.array([[ 102,  164,  226],
 [ 294,  468,  642],
 [ 486,  772, 1058]])

print('D^T = ',np.transpose(D))
print("")

E = np.sqrt(D)/2
print('E = ',E)
