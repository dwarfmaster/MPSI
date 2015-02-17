#!/usr/bin/python3
from math import sqrt;

def norm(l):
    i = len(l) - 1
    while i >= 0 and l[i] == 0:
        i -= 1
    if i < 0:
        return [0]
    else:
        return l[:i+1]

def multXp(a, p, coeff):
    l = [0]*p + a
    for i in range(p, len(l)):
        l[i] *= coeff
    return l

def addP(a, b):
    n = max(len(a),len(b))
    c = [0]*n
    for i in range(n):
        if i < len(a):
            c[i] = a[i]
        if i < len(b):
            c[i] += b[i]
    return c

def divEuclid(a, b):
    q = [0]*(len(a) - len(b) + 1)
    r = a
    while len(r) >= len(b):
        p = len(r) - len(b)
        c = r[-1]/b[-1]
        q[p] = c
        m = multXp(b, p, -c)
        r = addP(r, m)
        r = norm(r)
    return (q,r)

def compXp(a, p):
    l = [0]*((len(a) - 1) * p + 1)
    for i in range(len(a)):
        l[i*p] = a[i]
    return l

def polyCyclo(l):
    if len(l) == 0:
        return [-1, 1]
    p = l[0][0]
    ls = l[1:]
    for i in range(len(l)):
        p *= l[i][0] ** (l[i][1] - 1)
    poly = polyCyclo(ls)
    return divEuclid(compXp(poly, p), poly)[0]

def decomp(n):
    if n == 1:
        return []
    def joindecomp(d1, d2):
        d = d1
        for i in range(len(d2)):
            p = -1
            for j in range(len(d)):
                if d[j][0] == d2[i][0]:
                    p = j
                    break
            if p == -1:
                d.append(d2[i])
            else:
                d[p][1] += d2[i][1]
        return d

    s = int(sqrt(n))
    for d in range(2, s+1):
        if n%d == 0:
            return joindecomp(decomp(d), decomp(n//d))
    # n prime
    return [[n,1]]

def polyCyclo2(n):
    return polyCyclo(decomp(n))

def merge(l, out):
    for a in out:
        if not a in l:
            l.append(a)

def quicksort(l):
    if len(l) <= 1:
        return l
    a = l[0]
    l1 = [x for x in l if x < a]
    m  = [x for x in l if x == a]
    l2 = [x for x in l if x > a]
    return quicksort(l1) + m + quicksort(l2)

if __name__ == "__main__":
    coeffs = []
    test = True
    for n in range(2,100):
        cfs = polyCyclo2(n)
        if test:
            for a in cfs:
                if not a in [-1, 0, 1]:
                    test = False
                    print("First other :", n)
                    break
        merge(coeffs, cfs)
    print(quicksort(coeffs))


