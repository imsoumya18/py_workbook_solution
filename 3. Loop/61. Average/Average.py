x = int(input("Enter: "))
if x == 0:
    print("Wrong input.")
else:
    s = 0
    count = 0
    while x != 0:
        s = s + x
        x = int(input("Enter: "))
        count = count + 1

print("Average- ", s/count)
