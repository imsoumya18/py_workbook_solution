m,d = input('Enter month:'), int(input('Enter day:'))

if (m=='January' and d==1):
    print('It\'s New Year\'s Day.')
elif (m=='July' and d==1):
    print('It\'s Canada Day.')
elif (m=='December' and m==25):
    print('It\'s Christmas Day.')
else:
    print('It\'s not a holiday.')