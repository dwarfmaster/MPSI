#!/usr/bin/python3
# vim:set foldmethod=marker:
from copy import copy;

# {{{ Utils
def make_vect(n, v):
    r = []
    for i in range(n):
        r += [v]
    return r
# }}}

# {{{ Question 1 : estPermutation
def estPermutation(t):
    bs = make_vect(len(t), False)
    for i in range(len(t)):
        if t[i] > len(t):
            return False
        elif bs[t[i] - 1]:
            return False
        else:
            bs[t[i] - 1] = True
    return True

# Tests
print("Expect True : ", estPermutation([3, 4, 2, 1]))
print("Expect False : ", estPermutation([1, 3]))
print("Expect False : ", estPermutation([1, 2, 3, 2]))
# }}}

# {{{ Question 2 : composer
def composer(t, u):
    if len(t) != len(u):
        raise "Error : invalid composition"
    c = make_vect(len(t), 0)
    for i in range(len(t)):
        c[i] = t[u[i] - 1]
    return c

# Tests
print("Expect [1, 2] :", composer([2,1], [2,1]))
print("Expect [2, 1, 3] :", composer([2, 3, 1], [1, 3, 2]))
# }}}

# {{{ Question 3 : inverser
def inverser(t):
    inv = make_vect(len(t), 0)
    for i in range(len(t)):
        inv[t[i] - 1] = i + 1
    return inv

# Tests
print("Expect [2, 1] :", inverser([2,1]))
# }}}

# {{{ Question 4
# Permutation ordre 1 : [1, 2, 3, 4, 5]
# Permutation ordre n : [n, 1, 2, ..., n - 2, n - 1]
# }}}

# {{{ Question 5 : ordre
def ordre(t):
    def check_ident(t):
        for i in range(len(t)):
            if t[i] != i + 1:
                return False
        return True
    l = copy(t)
    n = 1
    while not check_ident(l):
        l = composer(l, t)
        n += 1
    return n

# Test
print("Expect 2 :", ordre([2, 1]))
print("Expect 1 :", ordre([1, 2, 3, 4]))
print("Expect 3 :", ordre([3, 1, 2]))
# }}}

# {{{ Question 6 : periode
def periode(t, i):
    n = 1
    l = copy(t)
    while l[i - 1] != i:
        l = composer(l, t)
        n += 1
    return n

# Tests
print("Expect 1 :", periode([1, 2, 3], 1))
print("Expect 2 :", periode([3, 2, 1], 1))
print("Expect 3 :", periode([3, 1, 2], 1))
# }}}

# {{{ Question 7 : estDansOrbite
def estDansOrbite(t, i, j):
    l = copy(t)
    while l[i - 1] != i:
        if l[i - 1] == j:
            return True
        l = composer(l, t)
    return False

# Test
print("Expect False :", estDansOrbite([3, 2, 1], 1, 2))
print("Expect True :", estDansOrbite([3, 1, 2], 1, 2))
# }}}

# {{{ Question 8 : estTransposition
def estTransposition(t):
    n = 0
    for i in range(len(t)):
        if t[i] != i + 1:
            n += 1
    return n == 2

# Tests
print("Expect False :", estTransposition([4, 3, 2, 1]))
print("Expect True :", estTransposition([2, 1, 3, 4, 5]))
# }}}

# {{{ Question 9 : estCycle
def estCycle(t):
    orb = []
    for i in range(1, len(t)+1):
        if periode(t, i) != 1:
            orb.append(i)
    if len(orb) == 0:
        return False
    for j in range(1, len(orb)):
        if not estDansOrbite(t, orb[0], orb[j]):
            return False
    return True

# Tests
print("Expect True :", estCycle([4,1,2,3]))
print("Expect False :", estCycle([2,1,4,3]))
print("Expect True :", estCycle([1,2,3,6,4,5]))
# }}}

# {{{ Question 10 : periodes
def periodes(t):
    ps = make_vect(len(t), 0)
    for i in range(len(t)):
        # Si l'élément est dans un cycle parcouru
        if ps[i] != 0:
            continue
        # Sinon, on parcourt le cycle
        ls = [i]
        j = i
        while t[j] != i + 1:
            j = t[j] - 1
            ls += [j]
        for a in ls:
            ps[a] = len(ls)
    return ps

# Tests
print("Expect [3,3,3] :", periodes([3, 1, 2]))
print("Expect [1,2,2] :", periodes([1, 3, 2]))
print("Expect [1,2,3,3,2,3] :", periodes([1, 5, 4, 6, 2, 3]))
# }}}

# {{{ Question 11 : itererEfficace
def itererEfficace(t, k):
    ps = periodes(t)
    rs = [divmod(k,p)[1] for p in ps]
    r = 0
    for i in range(1, len(ps)):
        r = max(r, rs[i])
    ret = copy(t)
    l = list(range(1,len(t)+1))
    n = 0
    while n <= r:
        for i in range(len(rs)):
            if n == rs[i]:
                ret[i] = l[i]
        l = composer(l, t)
        n += 1
    return ret

# Tests
print("Expect [2, 1] :", itererEfficace([2, 1], 201))
print("Expect [1, 2, 3] :", itererEfficace([3, 1, 2], 66))
# }}}

# {{{ Question 12
# [3, 1, 2, 8, 4, 5, 6, 7] -> taille 8, ordre 15
# }}}

# {{{ Question 13 : pgcd
def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, divmod(a,b)[1])

# Test
print("Expect 1 :", pgcd(15, 2))
print("Expect 3 :", pgcd(15, 6))
# }}}

# {{{ Question 14 : ppcm
def ppcm(a, b):
    return (a*b) // pgcd(a,b)

# Tests
print("Expect 30 :", ppcm(6, 5))
# }}}

# {{{ Question 15 : ordreEfficace
def ordreEfficace(t):
    calc = []
    ordre = 1
    ps = periodes(t)
    for p in ps:
        if p in calc:
            continue
        ordre = ppcm(ordre, p)
        calc.append(p)
    return ordre

# Tests
print("Expect 2 :", ordreEfficace([2, 1]))
print("Expect 1 :", ordreEfficace([1, 2, 3, 4]))
print("Expect 3 :", ordreEfficace([3, 1, 2]))
# }}}

