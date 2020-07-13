p = float(input('Enter pressure(Pascal) exerted by the gas:'))
v = float(input('Enter volume(Litres) of the gas:'))
t = float(input('Enter temperature(Kelvin) of the gas:'))
r = 8.314

n = (p*v)/(r*t)

print('Number of moles of the gas=',n)