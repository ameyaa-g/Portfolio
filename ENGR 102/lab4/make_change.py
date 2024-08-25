# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ameya Gopinath
#               Javier Dominguez
#               Leonard Montemayor
#               Guadalupe Medrano
# Section:      M02
# Assignment:   Lab 4
# Date:         9 18 2023

# input dollar and cost
dollar = float(input("How much did you pay?"))
cost = float(input("How much did it cost?"))

#calculate change
change = dollar - cost

# convert dollars to cents to make divison easier
cent = dollar * 100
cost *= 100
chang = cent - cost

# divide the cent by 25 to get quarters
quart = int(chang // 25)

# remove from original
cent = chang - (25 * quart)

# do the same for dime, cent, and nickel
dime = int(cent // 10)
cent = cent - (10 * dime)
nickel = int(cent // 5)
cent = int(cent - (10 * nickel))

# print the answers, changing the answers if they're singular
print(f"You received ${change:0.2f} in change. That is...")
if (quart == 1):
    print(f"{quart} quarter")
elif (quart > 1):
    print(f"{quart} quarters")

if (dime == 1):
    print(f"{dime} dime")
elif (dime > 0):
    print(f"{dime} dimes")

if (nickel == 1):
    print(f"{nickel} nickel")
elif (nickel > 0):
    print(f"{nickel} nickels")

if (cent == 1):
    print(f"{cent} penny")
elif (cent > 0):print(f"{cent} pennies")



