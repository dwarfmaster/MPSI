#!/usr/bin/python3

def mult(a):
    return (lambda x: a*x)

print(mult(3)(5))

