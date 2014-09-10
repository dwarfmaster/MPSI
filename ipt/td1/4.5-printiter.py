#!/usr/bin/python3

def carre(n):
    m = 2*n
    for y in range(0, n):
        print(m*'*-*')

def table(n):
    for y in range(n, 15*n+1, n):
        print("|", y, "|")

carre(5)
table(4)

