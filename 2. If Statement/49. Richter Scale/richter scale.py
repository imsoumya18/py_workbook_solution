m = float(input('Enter the magnitude in Richter scale:'))

if (m<2.0):
    print('Micro.')
elif (2.0<m<=3.0):
    print('Very minor.')
elif (3.0<m<=4.0):
    print('Minor.')
elif (4.0<m<=5.0):
    print('Light.')
elif (5.0<m<=6.0):
    print('Moderate.')
elif (6.0<m<=7.0):
    print('Strong.')
elif (7.0<m<=8.0):
    print('Major.')
elif (8.0<m<=10.0):
    print('Great.')
elif (m>10.0):
    print('Meteoric.')