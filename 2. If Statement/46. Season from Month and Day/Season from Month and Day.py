m,d = input('Enter the month:'), int(input('Enter the day:'))

if (m=='April' or m=='May'):
    print('Spring.')
elif (m=='July' or m=='August'):
    print('Summer.')
elif (m=='October' or m=='November'):
    print('Fall.')
elif (m=='January' or m=='February'):
    print('Winter.')
elif (m=='March' and d>=20):
    print('Spring.')
elif (m=='June' and d>=21):
    print('Summer.')
elif (m=='September' and d>=22):
    print('Fall.')
else:
    print('Winter.')