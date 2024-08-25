# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 6
# Date:         10 03 2023

# input the two integer
int1 = int(input("Enter an integer:"))
int2 = int(input("Enter another integer:"))
j = 1
# the loop while 100
while j <= 100:
    # if they're divisible by both integers
    if (j % (int1 * int2) == 0):
        print("Howdy Whoop")
    # if they're divisible by the first integers
    elif (j % int1 == 0):
        print("Howdy")
    # if they're divisible by the second integers
    elif (j % int2 == 0):
        print("Whoop")
    # if they're not divisible, just print the number
    else:
        print(j)
    # increment j
    j = j + 1



