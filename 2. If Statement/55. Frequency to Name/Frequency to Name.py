f = float(input('Enter the frequency:'))

if (f < 3 * 10 ** 9):
    print('Radio waves.')
elif (3 * 10 ** 9 <= f < 3 * 10 ** 12):
    print('Microwaves.')
elif (3 * 10 ** 12 <= f < 4.3 * 10 ** 14):
    print('Infrared light.')
elif (4.3 * 10 ** 14 <= f < 7.5 * 10 ** 14):
    print('Visible light.')
elif (7.5 * 10 ** 14 <= f < 3 * 10 ** 17):
    print('Ultraviolet light.')
elif (3 * 10 ** 17 <= f < 3 * 10 ** 19):
    print('X rays.')
elif (f >= 3 * 10 ** 19):
    print('Gamma rays.')
