yr = int(input("Enter a year: "))
if(yr%4==0):
    if(yr%100==0):
        if(yr%400==0):
            print("It is leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")