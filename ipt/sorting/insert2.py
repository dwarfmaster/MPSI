#!/usr/bin/python3

from random import shuffle, randint
nb = 5000

def perm(a, i1, i2):
    a[i1], a[i2] = a[i2], a[i1]

def pla_per(a, j):
    i = j
    while i > 0 and a[i-1] > a[i]:
        perm(a, i-1, i)
        i -= 1

def sort_insert(a):
    for i in range(1, len(a)):
        pla_per(a, i)

success = 0
for i in range(nb):
    size = randint(1, 50)
    a = list(range(size))
    shuffle(a)
    sort_insert(a)
    if a == list(range(size)):
        success += 1

print("Successes : ", success, "/", nb," [", 100*success/nb, "%]", sep="")

