#!/usr/bin/python3

def nbracines(a, b, c):
    if a == 0:
        print("Le coefficient dominant est nul, ce n'est pas un trinome !")
        return
    d = b*b - 4*a*c
    k = 2
    if abs(d) < 1e-10:
        k = 1
        d = 0
    elif d < 0:
        k = 0
    print("Le polynome " + str(a) + "X^2 + " + str(b) + "X + " + str(c) + " admet " + str(k) + " racines distinctes (det = " + str(d) + ")")

a = float(input("Entrez le coefficient dominant du trinome : "))
b = float(input("Entrez le coefficient d'ordre 1 du trinome : "))
c = float(input("Entrez la constante du trinome : "))
nbracines(a, b, c)
nbracines(0, 3, 1)
nbracines(1, 0.2, 0.01)

