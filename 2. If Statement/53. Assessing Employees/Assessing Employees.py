r = float(input('Enter rating of employee:'))

if (r==0.0):
    print('Unacceptable performance and raise=$',0)
elif (r==0.4):
    print('Acceptable performance and raise=$',2400*r)
elif (r>=0.6):
    print('Meritorious performance and raise=$',2400*r)
else:
    print('Wrong input.')