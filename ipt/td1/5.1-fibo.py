#!/usr/bin/python3

def fibo(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n1 = 0
        n2 = 1
        for x in range(2, n + 1):
            n3 = n2 + n1
            n1 = n2
            n2 = n3
        return n2

def fibodiv(d):
    n1 = 0
    n2 = 1
    n = 1
    while n2 % d != 0:
        n = n + 1
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    return n

print(fibo(73))
print(fibodiv(25))
print(fibodiv(150))

