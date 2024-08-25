
time = input("Enter the time: ")

type = int(input("Choose the clock type (12 or 24): "))
allowed = False
proper = 'abcdeghkmnopqrsuvwxyz@$&*='
chara = input("Enter your preferred character: ")
while allowed == False:
    if chara in proper:
        allowed = True
    else:
        chara = input("Character not permitted! Try again: ")

print()




num1 = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
num2 = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
num3 = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
num4 = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
pora =    [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
mlist = [['M', ' ', ' ', ' ', 'M'],
       ['M', 'M', ' ', 'M', 'M'],
       ['M', ' ', 'M', ' ', 'M'],
       ['M', ' ', ' ', ' ', 'M'],
       ['M', ' ', ' ', ' ', 'M']]





def coorzero(num, chara):
    if chara == '':
        chara = '0'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][0] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][2] = chara
    num[3][0] = chara
    num[3][2] = chara
    num[4][0] = chara
    num[4][1] = chara
    num[4][2] = chara

def coorone(num, chara):
    if chara == '':
        chara = '1'
    num[0][1] = chara
    num[1][0] = chara
    num[1][1] = chara
    num[2][1] = chara
    num[3][1] = chara
    num[4][0] = chara
    num[4][1] = chara
    num[4][2] = chara

def coortwo(num, chara):
    if chara == '':
        chara = '2'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][0] = chara
    num[4][0] = chara
    num[4][1] = chara
    num[4][2] = chara

def coorthree(num, chara):
    if chara == '':
        chara = '3'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][2] = chara
    num[4][0] = chara
    num[4][1] = chara
    num[4][2] = chara

def coorfour(num, chara):
    if chara == '':
        chara = '4'
    num[0][0] = chara
    num[0][2] = chara
    num[1][0] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][2] = chara
    num[4][2] = chara

def coorfive(num, chara):
    if chara == '':
        chara = '5'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][0] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][2] = chara
    num[4][0] = chara
    num[4][1] = chara
    num[4][2] = chara

def coorsix(num, chara):
    if chara == '':
        chara = '6'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][0] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][0] = chara
    num[3][2] = chara
    num[4][0] = chara
    num[4][1] = chara
    num[4][2] = chara

def coorseven(num, chara):
    if chara == '':
        chara = '7'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][2] = chara
    num[2][2] = chara
    num[3][2] = chara
    num[4][2] = chara

def cooreight(num, chara):
    if chara == '':
        chara = '8'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][0] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][0] = chara
    num[3][2] = chara
    num[4][0] = chara
    num[4][1] = chara
    num[4][2] = chara

def coornine(num, chara):
    if chara == '':
        chara = '9'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][0] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][2] = chara
    num[4][0] = chara
    num[4][1] = chara
    num[4][2] = chara

def p(num):
    chara = 'P'
    num[0][0] = chara
    num[0][1] = chara
    num[0][2] = chara
    num[1][0] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][0] = chara
    num[4][0] = chara

def a(num):
    chara = 'A'
    num[0][1] = chara
    num[1][0] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][0] = chara
    num[3][2] = chara
    num[4][0] = chara
    num[4][2] = chara

def m(num):
    chara = 'M'
    num[0][0] = chara
    num[0][2] = chara
    num[1][2] = chara
    num[1][0] = chara
    num[1][2] = chara
    num[2][0] = chara
    num[2][1] = chara
    num[2][2] = chara
    num[3][0] = chara
    num[3][2] = chara
    num[4][0] = chara
    num[4][2] = chara


after12 = False
twelve = False
single = False
tlist = time.split(":")
if type == 12:
    twelve = True
    if int(tlist[0]) > 12:
        hour = int(tlist[0]) % 12
        after12 = True
    elif int(tlist[0]) == 0:
        tlist[0] = '12'
        hour = int(tlist[0])
    else:
        hour = int(tlist[0])
    if hour < 10:
        single = True
        tothour = str(hour) + "0"
    else:
        after12 = False
        tothour = str(hour)
    tlist[0] = tothour
elif type == 24:
    if int(tlist[0]) > 24:
        hour = int(tlist[0]) % 24
        tothour = str(hour)
        tlist[0] = tothour

if tlist[0][0] == "1":
    coorone(num1, chara)
elif tlist[0][0] == "2":
    coortwo(num1, chara)
elif tlist[0][0] == "3":
    coorthree(num1, chara)
elif tlist[0][0] == "4":
    coorfour(num1, chara)
elif tlist[0][0] == "5":
    coorfive(num1, chara)
elif tlist[0][0] == "6":
    coorsix(num1, chara)
elif tlist[0][0] == "7":
    coorseven(num1, chara)
elif tlist[0][0] == "8":
    cooreight(num1, chara)
elif tlist[0][0] == "9":
    coornine(num1, chara)
else:
    coorzero(num1, chara)

if tlist[0][1] == "1":
    coorone(num2, chara)
elif tlist[0][1] == "2":
    coortwo(num2, chara)
elif tlist[0][1] == "3":
    coorthree(num2, chara)
elif tlist[0][1] == "4":
    coorfour(num2, chara)
elif tlist[0][1] == "5":
    coorfive(num2, chara)
elif tlist[0][1] == "6":
    coorsix(num2, chara)
elif tlist[0][1] == "7":
    coorseven(num2, chara)
elif tlist[0][1] == "8":
    cooreight(num2, chara)
elif tlist[0][1] == "9":
    coornine(num2, chara)
else:
    if twelve == True:
        single = True
    else:
        coorzero(num2, chara)

if tlist[1][0] == "0":
    coorzero(num3, chara)
elif tlist[1][0] == "1":
    coorone(num3, chara)
elif tlist[1][0] == "2":
    coortwo(num3, chara)
elif tlist[1][0] == "3":
    coorthree(num3, chara)
elif tlist[1][0] == "4":
    coorfour(num3, chara)
elif tlist[1][0] == "5":
    coorfive(num3, chara)
elif tlist[1][0] == "6":
    coorsix(num3, chara)
elif tlist[1][0] == "7":
    coorseven(num3, chara)
elif tlist[1][0] == "8":
    cooreight(num3, chara)
elif tlist[1][0] == "9":
    coornine(num3, chara)

if tlist[1][1] == "0":
    coorzero(num4, chara)
elif tlist[1][1] == "1":
    coorone(num4, chara)
elif tlist[1][1] == "2":
    coortwo(num4, chara)
elif tlist[1][1] == "3":
    coorthree(num4, chara)
elif tlist[1][1] == "4":
    coorfour(num4, chara)
elif tlist[1][1] == "5":
    coorfive(num4, chara)
elif tlist[1][1] == "6":
    coorsix(num4, chara)
elif tlist[1][1] == "7":
    coorseven(num4, chara)
elif tlist[1][1] == "8":
    cooreight(num4, chara)
elif tlist[1][1] == "9":
    coornine(num4, chara)

if after12 == True:
    p(pora)
elif after12 == False:
    a(pora)


for i in range(len(num1)):
    for j in range(len(num1[i])):
        if j == (len(num1[i]) - 1):
            print(f'{num1[i][j]}', end=" ")
        else:
            print(f'{num1[i][j]}', end="")
    if single is False or twelve is False:
        for j in range(len(num2[i])):
            if j == (len(num1[i]) - 1):
                print(f'{num2[i][j]}', end=" ")
            else:
                print(f'{num2[i][j]}', end="")
    if i == 1 or i == 3:
        print(":", end=" ")
    else:
        print('', end="  ")
    for j in range(len(num3[i])):
        if j == (len(num1[i]) - 1):
            print(f'{num3[i][j]}', end=" ")
        else:
            print(f'{num3[i][j]}', end="")
    for j in range(len(num4[i])):
        if j == (len(num1[i]) - 1):
            if twelve == False:
                print(f'{num4[i][j]}', end="")
            else:
                print(f'{num4[i][j]}', end=" ")
        else:
            print(f'{num4[i][j]}', end="")
    if twelve == True:
        for j in range(len(pora[i])):
            if j == (len(pora[i]) - 1):
                print(f'{pora[i][j]}', end=" ")
            else:
                print(f'{pora[i][j]}', end="")
        for j in range(len(mlist[i])):
            print(f'{mlist[i][j]}', end="")
    print()





