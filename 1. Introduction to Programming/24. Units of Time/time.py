d = int(input('Enter number of days:'))
h = int(input('Enter number of hours:'))
m = int(input('Enter number of minutes:'))
s = int(input('Enter number of seconds:'))

fs = d*86400+d*3600+m*60+s

print('Total time=',fs,'seconds')