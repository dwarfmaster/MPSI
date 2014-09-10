#!/usr/bin/python3
import math

def isprim(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

n = int(input("Entrez un nombre : "))
if isprim(n):
    print(n, "est premier.")
else:
    print(n, "n'est pas premier.")

