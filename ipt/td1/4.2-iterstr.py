#!/usr/bin/python3

def occurences(chaine, lettre):
    n = 0
    for l in list(chaine):
        if l == lettre:
            n = n + 1
    return n

def voyelles(chaine):
    n = 0
    for l in list(chaine):
        if l in {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}:
            n = n + 1
    return n

chaine = input("Entrez un texte : ")
lettre = input("Entrez une lettre : ")
while len(lettre) != 1:
    print(lettre, "n'est pas une lettre !")
    lettre = input("Entrez une lettre : ")

print(occurences(chaine, lettre), lettre, "dans", chaine)
print(voyelles(chaine), "voyelles dans", chaine)

