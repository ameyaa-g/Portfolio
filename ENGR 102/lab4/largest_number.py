# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 4
# Date:         07 011 2023

# inputting the numbers
num1 = input("Enter number 1: ")
num2 = input(" \nEnter number 2: ")
num3 = input("\nEnter number 3: \n")

# converting string to float
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

def largest_num ():
    # if number 1 is the biggest
    if (num1 > num2 and num1 > num3):
        print("The largest number is", num1)
    # if number 2 is the biggest
    elif(num2 > num1 and num2 > num3):
        print("The largest number is", num2)
    # if number 3 is the biggest
    elif (num3 > num1 and num3 > num2):
        print("The largest number is", num3)
    # if one of the numbers are the same as another
    elif(num2 == num1):
        # check whether the other number is the bigger one
        if(num2 >= num3):
            print("The largest number is", num2)
        else:
            print("The largest number is", num3)
    # compare for each number
    elif(num2 == num3):
        if (num1 >= num3):
            print("The largest number is", num1)
        else:
            print("The largest number is", num3)

    elif (num1 == num3):
        if (num2 >= num3):
            print("The largest number is", num2)
        else:
            print("The largest number is", num3)

# execute the function
largest_num()