#!/usr/bin/python3

def difference(A, B):
    C = set()
    for x in A:
        if not x in B:
            C = C | { x }
    return C

def differencesymetrique(A, B):
    return difference(A, B) | difference(B, A)

A = {"ed", 4, 6, "f", 56, 1.2}
B = {"gf", 6, 5, 34, "f", 1.2}
print(difference(A,B))
print(A - B)
print(differencesymetrique(A, B))
print(A ^ B)

