plate = input("Enter plate number: ")

if (len(plate) == 6 and
        'A' <= plate[0] <= 'Z' and
        'A' <= plate[1] <= 'Z' and
        'A' <= plate[2] <= 'Z' and
        0 <= int(plate[3]) <= 9 and
        0 <= int(plate[4]) <= 9 and
        0 <= int(plate[5]) <= 9):
    print("It's an older plate.")
elif (len(plate) == 7 and
      0 <= int(plate[0]) <= 9 and
      0 <= int(plate[1]) <= 9 and
      0 <= int(plate[2]) <= 9 and
      0 <= int(plate[3]) <= 9 and
      'A' <= plate[4] <= 'Z' and
      'A' <= plate[5] <= 'Z' and
      'A' <= plate[6] <= 'Z'):
    print("It's a new plate.")
else:
    print("This is not a valid plate.")
