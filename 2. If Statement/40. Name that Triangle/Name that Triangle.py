a,b,c = float(input('Enter length of first side:')),float(input('Enter length of first side:')),float(input('Enter length of first side:'))

if(a==b and b==c):
    print('Equilateral')
elif(a==b or b==c or c==a):
    print('Isosceles')
else:
    print('Scalene')