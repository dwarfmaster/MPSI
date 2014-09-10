#!/usr/bin/python3

def pge3(a, b, c):
    return max(a, max(b,c))

def pge5(a, b, c, d, e):
    return pge3(max(a,b), c, max(d, e));

a = int(input("Entrez un premier nombre : "))
b = int(input("Entrez un deuxieme nombre : "))
c = int(input("Entrez un troisieme nombre : "))
d = int(input("Entrez un quetrieme nombre : "))
e = int(input("Entrez un cinquieme nombre : "))
print("Le plus grand est", pge5(a,b,c,d,e))

