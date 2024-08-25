# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 4
# Date:         9 011 2023

import math

# input the day
day = input("Please enter a positive value for day:")
day = int(day)

# the minimum additional gadgets and constants at the end of each stage
min50 = (40 * (40 + 1) // 2)
min110 = (min50 + (10 * 100 + 50 * 40))

# rate
rate10 = (10 * day)

# if statements
if 0 < day <= 10:
    # at or before day 10
    print("The sum total number of gadgets produced on day", day, "is", 10 * day)
elif 50 > day > 10:
    # before day 50 and after day 10, where the new rate is increasing by 1 everyday
    dayrate = day - 10

    print("The sum total number of gadgets produced on day", day, "is", rate10 + (dayrate * (dayrate + 1) // 2))
elif 101 > day >= 50:
    # before day 101 and after 10
    dayrate = day - 50
    print("The sum total number of gadgets produced on day", day, "is", (min50 + (10 * day + dayrate * 40)))
elif day >= 101:
    print("The sum total number of gadgets produced on day", day, "is", min110)
else:
    print("You entered an invalid number!")

