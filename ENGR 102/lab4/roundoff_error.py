
############ Part A ############

TOL = 1 * 10 ** -10
a = 1 / 7
print(f'a = {a}')
b = a * 7
# this should be 1, because (1 / 7) * 7 = 1
print(f'b = a * 7 = {b}')

c = 2 * a
d = 5 * a
f = c + d
# this does not equal 1, even though it should be, because it rounds off the division of 2/7 and 5/7 and doesn't equal 1
print(f'f = 2 * a + 5 * a = {f}')


from math import sqrt
TOL = 1 * 10 ** -10
x = sqrt(1 / 3)
print(f'x = {x}')
y = x * x * 3
# this is 1, because at this point, this is multiplied by a whole number
print(f'y = x * x * 3 = {y}')
z = x * 3 * x
# this is not 1, because it rounds off the 3 * sqrt (1 / 3) and then multiplies the sqrt(1 / 3) again
print(f'z = x * 3 * x = {z}')

############ Part B ############

TOL = 1 * 10 ** -10
# check if b and f are equal within specified tolerance
if abs(b - f) < TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are NOT equal within tolerance of {TOL}')

if abs(y - z) < TOL:
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print(f'y and z are NOT equal within tolerance of {TOL}')

############ Part C ############

m = 0.1
print(f'm = {m}')
n = 3 * m
print(f'n = 3 * m = 0.3 {n==0.3}')
p = 7 * m
print(f'p = 7 * m = 0.7 {p==0.7}')
q = n + p
print(f'q = n + p = 1 {q==1}')




