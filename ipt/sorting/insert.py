#!/usr/bin/python3

lst = [4, 1, 2, 6, 0, 3, 5]

def intercal(a, i):
    j = 0
    while a[j] < a[i]:
        j += 1
    return j

print(intercal(lst, 2))
print(intercal(lst, 6))

def decalage(a, j, i):
    if i == len(a) - 1:
        i = len(a) - 2
    for k in range(i, j - 1, -1):
        a[k+1] = a[k]

def placement(a, i):
    x = a[i]
    j = intercal(a, i)
    decalage(a, j, i-1)
    a[j] = x

def tri_insertion(a):
    for i in range(len(a)):
        placement(a, i)

tri_insertion(lst)
print(lst)


