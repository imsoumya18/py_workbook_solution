x = input('Enter position of the square:')

if (x[0]=='a' or x[0]=='c' or x[0]=='e' or x[0]=='g'):
    if (int(x[1])%2==0):
        print('White.')
    else:
        print('Black.')
else:
    if (int(x[1])%2==0):
        print('Black.')
    else:
        print('White.')