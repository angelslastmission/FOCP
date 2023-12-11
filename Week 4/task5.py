def multiply(x, y=None):
    if y is None:
        return x*x
    else:
        return x*y
    
print(multiply(2))
print(multiply(2,4))