from math import sqrt
s1 = float(input('Enter length of first side:'))
s2 = float(input('Enter length of second side:'))
s3 = float(input('Enter length of third side:'))

s = (s1+s2+s3)/2

a = sqrt(s*(s-s1)*(s-s2)*(s-s3))

print('Area of the triangle=',a)