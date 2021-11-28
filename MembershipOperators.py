import math

a = [1, 2, 3, 4, 5, 6, 6]
print(a)
# to check for existence of b in a
b = 2
print(b in a)
print(b not in a)


# identity operators , == sign can be used
x = 312345678098765
y = 312345678098765
print(x is y)
print(x is not y)

if x is y:
    print("they are equal", x)
else:
    print("they are not equal")
