m = float(input('Enter mass in grams:'))
c = 4.186
t = float(input('Enter change in temperature:'))

q = m*c*t

print('Energy required=',q,'J')

kwh = q*2.777e-7

print('Electricity bill=',kwh*8.9,'cents')
