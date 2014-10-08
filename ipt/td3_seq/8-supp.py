#!/usr/bin/python3

def supph(a, i):
    l = []
    for j in range(0, len(a)):
        if i != j:
            l += [a[j]]
    return l

def supps(a, i):
    return a[0:i] + a[i+1:len(a)]

def suppc(a, i):
    return [ a[j] for j in range(0, len(a)) if j != i ]

print(supph("Helloo world !", 5))
print(supps("Helloo world !", 5))
print(suppc("Helloo world !", 5))

