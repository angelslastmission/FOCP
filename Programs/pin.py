pin = "1111"
count = 0
while count<3:
    pw = input("Enter a pin:")
    if pw == pin:
        print("Welcome:")
        break
    else:
        print("Sorry incorrect pin!")
        count = count + 1
        if count == 3:
            print("To many incorrect attempts")