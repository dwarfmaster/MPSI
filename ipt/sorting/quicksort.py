#!/usr/bin/python3

from random import shuffle, randint
nb = 5000

def quicksort(a):
    if len(a) <= 1:
        return a
    piv = a[0]
    l1 = []
    l2 = []
    lm = []
    for i in range(len(a)):
        if a[i] < piv:
            l1 += [a[i]]
        elif a[i] > piv:
            l2 += [a[i]]
        else:
            lm += [piv]
    return quicksort(l1) + lm + quicksort(l2)

if __name__ == "__main__":
    success = 0
    for i in range(nb):
        size = randint(1, 50)
        a = list(range(size))
        shuffle(a)
        a = quicksort(a)
        if a == list(range(size)):
            success += 1
    print("Successes : ", success, "/", nb," [", 100*success/nb, "%]", sep="")

