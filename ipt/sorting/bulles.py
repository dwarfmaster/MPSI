#!/usr/bin/python3

from random import shuffle, randint
nb = 5000

def swap_if(a, i):
    if a[i] > a[i+1]:
        a[i], a[i+1] = a[i+1], a[i]
        return 1
    else:
        return 0

def sort_pass(a):
    swaps = 0
    for i in range(len(a) - 1):
        swaps += swap_if(a, i)
    if swaps == 0:
        return False
    else:
        return True

def sort_bulles(a):
    ret = True
    while ret:
        ret = sort_pass(a)

if __name__ == "__main__":
    success = 0
    for i in range(nb):
        size = randint(1, 50)
        a = list(range(size))
        shuffle(a)
        sort_bulles(a)
        if a == list(range(size)):
            success += 1
    print("Successes : ", success, "/", nb," [", 100*success/nb, "%]", sep="")

