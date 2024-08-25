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

# input the coefficients
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

# if A is 0, there is no operator for B
if A == 0:
    Astr = ""

    if B == 0:
        Bstr = ""
    elif B == 1:
        Bstr = "x"
    elif B < 0:
        B = - B
        Bstr = f"- {B}x"
    else:
        Bstr = f"{B}x"

elif A == 1:
    Astr = "x^2"
elif A < 0 and A != -1:
    A = -A
    Astr = f"- {A}x^2"
elif (A == -1):
    Astr = "- x^2"
else:
    Astr = f"{A}x^2"

# when A equals to 0, the pre-existing code shouldn't be overridden
if (A != 0):
    # if B is 0, there is no operator before C
    if B == 0:
        Bstr = ""
        
        if C == 0:
            Cstr = ""
        elif C == 1:
            Cstr = " 1"
        elif C < 0:
            C = - C
            Cstr = f" - {C}"
        else:
            Cstr = f" {C}"

    elif B == 1:
        Bstr = " + x"
    elif B < 0 and B != -1:
        B = - B
        Bstr = f" - {B}x"
    elif (B == -1):
        Bstr = " - x"
    else:
        Bstr = f" + {B}x"

# when B equals to 0, the pre-existing code shouldn't be overridden
if(B != 0):
    if C == 0:
        Cstr = ""
        if C == 0 and B == 0:
            Cstr = ""
    elif C == 1:
        Cstr = " + 1"
    elif C < 0 and B != -1:
        C -= C
        Cstr = f" - {C}"
    else:
        Cstr = f" + {C}"

print("The quadratic equation is", Astr + Bstr + Cstr, "= 0")



