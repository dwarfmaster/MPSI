#!/usr/bin/python3

# f est la factorielle de n
def f(n):
    u = 1
    for x in range(1, n+1):
        u = u * x
    return u

print(f(0))
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

