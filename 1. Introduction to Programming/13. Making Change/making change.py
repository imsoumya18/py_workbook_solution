c = int(input("Enter the amount in cents="))

print("No. of toonies=",c//200)
c = c%200

print("No. of loonies=",c//100)
c = c%100

print("No. of quarters=",c//25)
c = c%25

print("No. of dimes=",c//10)
c = c%10

print("No. of nickels=",c//5)
c = c%5

print("No. of pennies=",c)