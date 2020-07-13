w = float(input('Enter wavelength in nanometer:'))

if (380<=w<450):
    print('Violet.')
elif (450<=w<495):
    print('Blue.')
elif (495<=w<570):
    print('Green.')
elif (570<=w<590):
    print('Yellow.')
elif (590<=w<620):
    print('Orange.')
elif (620<=w<=750):
    print('Red.')
else:
    print('The light is not visible.')