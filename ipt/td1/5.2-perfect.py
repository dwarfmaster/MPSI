#!/usr/bin/python3
import math

def divs(n):
    lst = list()
    sq = math.sqrt(n)
    for d in range(1, math.ceil(sq)):
        if n % d == 0:
            lst = lst + [d, n//d]
    if int(sq) == sq:
        lst = lst + [sq];
    return lst

def isperfect(n):
    dvs = divs(n)
    sm = 0
    for d in dvs:
        if d < n:
            sm = sm + d
    return (sm == n)

def perfects(n):
    lst = list()
    for i in range(1, n+1):
        if isperfect(i):
            lst = lst + [i]
    return lst

print(perfects(10000))

