x,y,z = int(input('Enter first integer:')),int(input('Enter second integer:')),int(input('Enter third integer:'))

b = max(x,y,z)
s = min(x,y,z)

print('The sorted integers:{0},{1},{2}'.format(s,x+y+z-b-s,b))