t = float(input('Enter air temperature in celsius:'))
if t<=10:
    v = float(input('Enter velocity of air in kmph:'))
    if v>=4.8:
        wci = 13.12 + 0.6215 * t - 11.37 * (v ** 0.16) + 0.3965 * t * (v ** 0.16)
        print('Wind chill index=',wci)
    else:
        print('WCI can\'t be calculated.')
else:
    print('WCI can\'t be calculated.')