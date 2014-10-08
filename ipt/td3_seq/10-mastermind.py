#!/usr/bin/python3
import random as rd;

def suppi(l, i):
    return l[0:i] + l[i+1:len(l)]

def suppe(l, r):
    ret = []
    for i in range(0, len(l)):
        if r == l[i]:
            ret += l[i+1:len(l)]
            break
        ret += [l[i]]
    return ret

def reponse(c, e):
    nn = 0
    nb = 0

    i = 0
    while i < len(c):
        if c[i] == e[i]:
            nn += 1
            e = suppi(e, i)
            c = suppi(c, i)
        else:
            i += 1

    i = 0
    while i < len(c):
        if c[i] in e:
            e = suppe(e, c[i])
            c = suppi(c, i)
            nb += 1
        else:
            i += 1

    return [nn, nb]

def gen_code():
    return [rd.randint(0,5),
            rd.randint(0,5),
            rd.randint(0,5),
            rd.randint(0,5)]

def input_value(i):
    nb = -1
    while nb not in list(range(0,6)):
        nb = int(input("Entrez la valeur " + str(i) + " : "))
    return nb

def input_code():
    cd = []
    for i in range(1,5):
        cd += [input_value(i)]
    return cd

def test(c, e):
    rep = reponse(c, e)
    print(e, "->", rep)
    return rep

if __name__ == "__main__":
    nb = 0
    code = []
    ret = [0,0]

    while nb not in [1,2]:
        nb = int(input("1 ou 2 joueurs ? "))
    if nb == 1:
        code = gen_code()
    else:
        print("Joueur 1, fermez les yeux !\nJoueur 2, entrez les valeurs.")
        code = input_code()

    print("Code obtenu. Début du jeu.")
    nb = 0
    while ret[0] != 4:
        ret = test(code, input_code())
        nb += 1

    print("Bravo, vous avez gagné en", nb, "coups !")

