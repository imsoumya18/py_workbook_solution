kp = float(input('Enter pressure in Kilopascal:'))

psi = kp/6.895
mer = kp*7.501
atm = kp/101.325

print('Pressure in PSI=',psi,'PSI')
print('Pressure in mercury=',mer,'Millimetre of mercury')
print('Pressure in atmosphere=',atm,'atmospheric pressure')