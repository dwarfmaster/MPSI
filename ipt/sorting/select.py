#!/usr/bin/python3

from random import shuffle, randint
nb = 5000

def minimum(a, start):
    mn = a[start]
    mnid = start
    for i in range(start + 1, len(a)):
        if a[i] < mn:
            mn = a[i]
            mnid = i
    return mnid

def swap(a, i1, i2):
    a[i1], a[i2] = a[i2], a[i1]

def sort_select(a):
    for i in range(0, len(a)):
        mn = minimum(a, i)
        swap(a, mn, i)

success = 0
for i in range(nb):
    size = randint(1, 50)
    a = list(range(size))
    shuffle(a)
    sort_select(a)
    if a == list(range(size)):
        success += 1

print("Successes : ", success, "/", nb," [", 100*success/nb, "%]", sep="")

