ap = 3.49
d = (3.49*60)/100

x = int(input('Enter the number of day old breads:'))

tap = x*ap
td = x*d
tp = tap-td

print('Actual price=%5.2f ,discount=%5.2f ,total price=%5.2f'%(tap,td,tp))