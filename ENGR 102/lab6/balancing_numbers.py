# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 6
# Date:         10 03 2023

n = int(input("Enter a value for n:"))


j = n - 1
sumlow = 0

# go down from the original number and add up all of them
while j != 0:
    sumlow = sumlow + j
    j = j - 1




r = 1
curnum = n + 1
sumhigh = 0
# have a flag for whether it is a balancing number or not
flag = False
nextnum = 0
# try for a little while, but if it isn't true, then stop
while r < 1000:

    # get the next number
    nextnum = curnum + 1
    # for testing
    # print(f'{curnum}, {nextnum}')
    # add it up
    sumhigh += curnum + nextnum
    # if the sum is the same, set flag to true and break. If not, keep going
    if (sumlow == sumhigh):
        flag = True
        break
    # increment the r value
    r = r + 1
    # append the next number after the previous
    curnum = curnum + 2

# I've been skipping half of the additions to avoid repeating current and next values
r = r * 2
# if it is true or false, print the respective statements
if flag == True:
    print(f"{n} is a balancing number with r={r}")
elif flag == False:
    print(f"{n} is not a balancing number")