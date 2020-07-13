from math import tan,pi

n = int(input('Enter no. of sides:'))
s = float(input('Length of each side:'))

a = (n*s*s)/(4*tan(pi/n))

print('Area of the polygon:',a)