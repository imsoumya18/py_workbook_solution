y = int(input("Enter the year: "))
m = int(input("Enter the month: "))
d = int(input("Enter the day: "))

y2 = y
m2 = m
d2 = d

def leap(a):
    if(a%4==0):
        if(a%100==0):
            if(a%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if(m==12 and d==31):
    y2 = y+1

if(d==31):
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10):
        m2 = m+1
    elif(m==12):
        m2 = 1
elif(d==30):
    if(m==4 or m==6 or m==9 or m==11):
        m2 = m+1
elif(d==28 and m==2 and (not leap(y))):
    m2 = m+1
elif(d==29 and m==2 and leap(y)):
    m2 = m+1

if(d==31):
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        d2 = 1
elif(d==30):
    if(m==2 or m==4 or m==6 or m==9 or m==11):
        d2 = 1
elif(d==28 and m==2 and (not leap(y))):
    d2 = 1
elif(d==29 and m==2 and leap(y)):
    d2 = 1
else:
    d2 = d+1


print('Next day is:',y2,'-',m2,'-',d2)