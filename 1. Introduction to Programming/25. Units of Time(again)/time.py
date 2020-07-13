sec = int(input('Enter the number of seconds:'))

d = int(sec/86400)
sec = sec%86400

h = int(sec/3600)
sec = sec%3600

m = int(sec/60)
sec = sec%60

print('{}:{:02d}:{:02d}:{:02d}'.format(d,h,m,sec))