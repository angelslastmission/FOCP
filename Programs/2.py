x = 5
def yelp(x,y):
    print(x)
    x = 7
    print(x)
    y = x
    return y

a = yelp(x,y)
print(y)
print(x)
print(y)
print(a)