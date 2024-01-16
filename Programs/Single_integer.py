#Functions are often used to validate input. Write a function that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise. Write a short program to test the function.

def check_value(num):
    if 0 < num <= 100:
        print(True)
    else:
        print(False)
    pass
    
    check_value(100)