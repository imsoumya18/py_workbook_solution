m,d = input('Enter the month:'), int(input('Enter the day:'))

if (m=='January'):
    if (d<20):
        print('Capricorn.')
    else:
        print('Aquarius.')
elif (m=='February'):
    if (d<19):
        print('Aquarius.')
    else:
        print('Pisces.')
elif (m=='March'):
    if (d<21):
        print('Pisces.')
    else:
        print('Aries.')
elif (m=='April'):
    if (d<20):
        print('Aries.')
    else:
        print('Taurus.')
elif (m=='May'):
    if (d<21):
        print('Taurus.')
    else:
        print('Gemini.')
elif (m=='June'):
    if (d<21):
        print('Gemini.')
    else:
        print('Cancer.')
elif (m=='July'):
    if (d<23):
        print('Cancer.')
    else:
        print('Leo.')
elif (m=='August'):
    if (d<23):
        print('Leo.')
    else:
        print('Virgo.')
elif (m=='September'):
    if (d<23):
        print('Virgo.')
    else:
        print('Libra.')
elif (m=='October'):
    if (d<23):
        print('Libra.')
    else:
        print('Scorpio.')
elif (m=='November'):
    if (d<22):
        print('Scorpio.')
    else:
        print('Sagittarius.')
else:
    print('Capricorn.')