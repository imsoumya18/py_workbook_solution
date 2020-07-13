f = int(input('Which system of units do you prefer? 1.Inches/Pounds or 2.Meter/Kilogram :'))

if f==1:
    w = float(input('Enter weight in pounds:'))
    h = float(input('Enter height in inches:'))

    bmi = (w*703)/(h*h)

    print('Your BMI is=',bmi)

elif f==2:
    w = float(input('Enter weight in kilograms:'))
    h = float(input('Enter height in meters:'))

    bmi = w/(h*h)

    print('Your BMI is=',bmi)

else:
    print('Wrong input!!!')