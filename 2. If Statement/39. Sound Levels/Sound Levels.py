x = float(input('Enter sound level in Decibels:'))

if (x<40):
    print('Sound is lower than a quiet room.')
elif(x==40):
    print('Sound level is like quite room.')
elif(x>40 and x<70):
    print('Sound level is between quiet room and alarm clock.')
elif(x==70):
    print('Sound is like alarm clock.')
elif(x>70 and x<106):
    print('Sund level is between alarm clock and gas lawnmower.')
elif(x==106):
    print('Sound level is like gas lawnmower.')
elif(x>106 and x<130):
    print('Sound level is between gas lawnmower and jackhammer.')
elif(x==130):
    print('Sound is like jackhammer.')
else:
    print('Wrong input!!!')