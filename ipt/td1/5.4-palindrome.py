#!/usr/bin/python3

def palindrome(chaine):
    chaine2 = ""
    for l in chaine:
        if l in {' ', '\n', '\t'}:
            chaine2 = chaine2 + l
    chaine2 = list(chaine2)
    l = len(chaine2)
    for i in range(0, l):
        if chaine2[i] != chaine2[l-i-1]:
            return False
    return True

print(palindrome(input("Entrez une phrase : ")))

