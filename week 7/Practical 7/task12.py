import math

roots = {n: math.sqrt(n) for n in range(1, 26)}  # Creating the roots dictionary

# Iterating over the contents of the roots dictionary
for num, sqrt in roots.items():
    print(f"The square root of {num} is {sqrt}")
