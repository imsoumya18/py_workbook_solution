price = [4.95, 9.95, 14.95, 19.95, 24.95]
print("Price        discount        new price\n")
for i in price:
    print(i, "        ", round(0.6 * i, 2), "        ", round(0.4 * i, 2), '\n')
