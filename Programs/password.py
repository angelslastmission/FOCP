upper = lower = special = num = False
char_lst = ['@','#','!']
num_lst = '0123456789'
BAD_PASSWORDS = ['password', 'garden', 'sisir', 'hello',]
while True:
    pw = input("Enter password: ")
    if pw in BAD_PASSWORDS:
        print("Sorry very weak password, try again!")
        continue
    if 8 <= len(pw) <=16:
        for i in pw:
            if i.isupper():
                upper = True
            if i.islower():
                lower = True
            if i in char_lst:
                special = True
            if i in num_lst:
                num = True

        if upper and lower and special and num:
            print("PW set successfully!")
            break
        else:
            print("PW does not meet criteria.")

    #     print("Successfully registered." if upper and lower and special and num
    #           else "PW does not meet criteria" )  

    else:
        print("Check password length!")