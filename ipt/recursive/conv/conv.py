#!/usr/bin/python3

from math import *;

def mmap(f, l):
    ls = []
    for i in range(len(l)):
        ls += f(l[i])
    return ls

def horner(l, p):
    if len(l) == 0:
        return 1
    elif len(l) == 1:
        return l[0]
    a  = l[0]
    b  = l[1]
    ls = l[1:]
    ls[0] = a*p + b
    return horner(ls, p)

def appBase(n):
    vals = mmap(chr, list(range(ord('0'), ord('9')+1)) + list(range(ord('a'), ord('z')+1)))
    return vals[n]

def stopbase(p, n):
    def mtopbase(p, n, l):
        if n == 0:
            return l
        q, r = divmod(n,p)[0], divmod(n,p)[1]
        return mtopbase(p, q, ([r] + l))
    return mmap(appBase, mtopbase(p,n,[]))

def topbase(p, n):
    return ''.join(stopbase(p,n))

def mapprox_10_to_p(x, p, epsilon):
    if x < 0:
        return ['-'] + mapprox_10_to_p(-x, p, epsilon)
    elif x > 1:
        return stopbase(p, floor(x)) + mapprox_10_to_p(x-floor(x), p, epsilon)
    n = floor(-log(epsilon, p)) + 1
    ls = []
    for i in range(1,n):
        x *= p
        f = floor(x)
        x -= f
        ls.append(appBase(f))
    return ['.'] + ls

def approx_10_to_p(x, p, epsilon):
    return ''.join(mapprox_10_to_p(x,p,epsilon))

