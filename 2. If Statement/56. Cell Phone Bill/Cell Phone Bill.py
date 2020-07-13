min = int(input("Enter total call minutes: "))
text = int(input("Enter total number of messages sent: "))
if(min>50):
    cc = 8+(min-50)*0.25
else:
    cc = 8
if(text>50):
    tc = 7+(text-50)*0.15
else:
    tc = 7
cost = (cc+tc+0.44)*1.05
print("Base charge: $",50)
if(min>50):
    print("Additional minutes charge: $",cc-8)
if(text>50):
    print("Additional text message charge: $",tc-7)
print("The 911 fee: $",0.44)
print("Tax: $",(cc+tc+0.44)*0.05)
print("Total bill amount: $",cost)