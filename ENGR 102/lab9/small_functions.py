# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 9
# Date:         11 02 2023


import math

def parta(rsphere, rcylin):
    # finding the equation, inputting the radius of the sphere and cylinder
    totvol = (4 * math.pi / 3) * (rsphere ** 2 - rcylin ** 2) ** (3/2)
    return totvol

def partb(n):
    # initialize list
    list = []
    # intialize sum
    sum = 0
    # loop from one to n
    for i in range(n):
        if i % 2 != 0:
            sum += i
            list.append(i)
            print(sum)
            if sum > n:
                sum = sum - list[0]
                del list[0]
                if sum > n:
                    sum = sum - list[0]
                    del list[0]
            if sum == n:
                break
    if len(list) <= 1:
        return False
    else:
        return list

def partc(char, name, location, email):
    # check which is longest: name, location, or email
    if (len(name)>=len(location) and len(name)>=len(email)):
        maxlen = len(name)
    elif (len(location)>=len(name) and len(location)>=len(email)):
        maxlen = len(location)
    elif (len(email)>=len(location) and len(email)>=len(name)):
        maxlen = len(email)
    # add the padding
    charlen = maxlen + 4
    charnum = char * (charlen + 2)
    # return the answer with formatting
    return(charnum+ f'\n{char}{name:^{charlen}}{char}\n{char}{location:^{charlen}}{char}\n{char}{email:^{charlen}}{char}\n'+charnum)


def partd(num):
    # sort the list
    num.sort()
    # initialize the max and min
    max = 0
    min = 10000
    # making the median
    if len(num) % 2 == 0:
         median = (num[len(num) // 2 - 1] + num[len(num) // 2]) / 2
    else:
        median = num[len(num) // 2]
    # checking the num, getting the max
    for i in num:
        if max < i:
            max = i
        if min > i:
            min = i
    return min, median, max

def parte(dist, time):
    # making a list of the velocities
    velocity = []
    for i in range(1, len(time)):
        # getting the change in distance
        d = dist[i] - dist[i - 1]
        # getting the change in time
        t = time[i] - time[i - 1]
        # getting the velocity
        v = d * t
        # append it to the list
        velocity.append(v)
    return velocity

def partf(num):
    # flag is for whenever there was EVER a 2027 number
    flag = False
    for i in num:
        for j in num:
            # if i + j is 2027
            if i + j == 2027:
                flag = True
                # return the product
                return i * j
    # if there wasn't, return
    if flag == False:
        return False

def partg(x, tol):
    n = 1
    term = 2 * x ** (2 * n - 1) / (2 * n - 1)
    sum = 0
    while abs(term) > tol:
        sum += term
        n += 1
        term = 2 * x ** (2 * n - 1) / (2 * n - 1)
    return sum

print(partg(0.99, 1e-12))