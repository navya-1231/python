from math import sqrt

a = 2
b = -5
c = 3

d = b*b-4*a*c

if d == 0:
    res = -b/(2*a)
elif d > 0:
    print('root 1 : ', (-b+sqrt(d)/2*a))
    print('root 2 : ', (-b-sqrt(d)/2*a))
else:
    print('imaginery roots')
