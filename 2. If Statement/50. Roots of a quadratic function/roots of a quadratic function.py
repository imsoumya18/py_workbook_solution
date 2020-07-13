from math import sqrt
a,b,c = float(input('Enter a:')), float(input('Enter b:')), float(input('Enter c:'))

d = b**2-4*a*c

if (d<0):
    print('There is no real root.')
elif (d==0):
    r = -b/2*a
    print('There is only one real root and that is:',r)
else:
    r1,r2 = (-b+sqrt(d))/(2*a),(-b-sqrt(d))/(2*a)
    print('There are two distinct real roots and those are:',r1,',',r2)