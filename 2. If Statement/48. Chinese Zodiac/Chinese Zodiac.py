x = int(input('Enter year:'))

if (x>2000):
    x = x-2000
else:
    x = 2000-x

y = x%12

if (y==0):
    print('Dragon.')
elif (y==1):
    print('Snake.')
elif (y==2):
    print('Horse.')
elif (y==3):
    print('Sheep.')
elif (y==4):
    print('Monkey.')
elif (y==5):
    print('Rooster.')
elif (y==6):
    print('Dog.')
elif (y==7):
    print('Pig.')
elif (y==8):
    print('Rat.')
elif (y==9):
    print('Ox.')
elif (y==10):
    print('Tiger.')
elif (y==11):
    print('Hare.')