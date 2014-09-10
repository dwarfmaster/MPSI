#!/usr/bin/python3

def valuation(p,n):
    a = 0;
    while n%p == 0:
        n = n / p
        a = a + 1
    return a

n = int(input("Entrez n "))
p = int(input("Entrez p "))
print(valuation(p,n))

