#!/usr/bin/python3

def supp(a, r):
    return [ e for e in a if e % r != 0 ]

def eras(n):
    l = list(range(2,n))
    ret = []
    while len(l) > 0:
        ret += [l[0]]
        l = supp(l, l[0])
    return ret

print(eras(1000))


