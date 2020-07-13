hy = float(input('Enter human year:'))
if hy<=2:
    dy = hy*10.5
else:
    dy = 21+(hy-2)*4
print('The equivalent Dog Years:',dy)