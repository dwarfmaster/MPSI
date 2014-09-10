#!/usr/bin/python3

def testpariteboolean_1(n):
    test = False
    q = n / 2
    if n // 2 == q:
        test = True
    return test

def testpariteboolean_2(n):
    test = True
    r = n % 2
    if r == 1:
        test = False
    return test

def testpariteboolean(n):
    return (n%2 == 0)

def printparite(n, b):
    if b:
        print(n, "est pair.")
    else:
        print(n, "est impair.")

n = int(input("Entrez un nombre "))
printparite(n, testpariteboolean(n))
printparite(n, testpariteboolean_1(n))
printparite(n, testpariteboolean_2(n))

