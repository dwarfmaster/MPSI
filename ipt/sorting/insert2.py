#!/usr/bin/python3

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

l = [1, 4, 5, 3, 2]
sort_insert(l)
print(l)

