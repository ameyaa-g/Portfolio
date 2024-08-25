# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 6
# Date:         10 03 2023
import math

# enter the integer
n = int(input("Enter a positive integer:"))

# open the loop
loop = 0
print(f"The Juggler sequence starting at {n} is: ")
while n != 1:
    # print the n
    print(n, end=", ")
    # if n is even, then take the sqrt of n
    if (n % 2 == 0):
        n = int(math.sqrt(n))
    # if n is odd, then take the sqrt of n and the power of 3
    elif (n % 2 != 0):
        n = int(math.sqrt(n) ** 3)
    # take a number of how often the loop loops
    loop = loop + 1

print("1")

print(f'It took {loop} iterations to reach 1')


i = 0
def h():
    i = 5
