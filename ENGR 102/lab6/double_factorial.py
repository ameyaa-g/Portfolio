# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 6.14
# Date:         9 27 2023

def doublefactorial(i):
    # fact starts as 1 to make sure that the output is never multiplied by 0
    fact = 1
    # the i will go down incrementally by 2 so the conditional is as long as it is greater than 0
    while i > 0:
        # multiply it
        fact = i * fact
        # go down by increments of 2
        i = i - 2
    return fact



