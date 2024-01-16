if 0 <= number <= 12:
    print(f"Multiplication table for {number}:")

    # Calculate and print the table
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
else:
    print("Please enter a valid number between 0 and 12.")