#!/usr/bin/python3
from random import randint

lst = [1, 4, 6, 2, 7, 8, 9, 10, 4, 6, 1]
print(lst)

########## Recherche d'un element ###########
def search_truth(x, a):
    for e in a:
        if e == x:
            return True
    return False

def search_id(x, a):
    for i in range(len(a)):
        if x == a[i]:
            return i
    return None

def search_pos(x, a):
    ids = []
    for i in range(len(a)):
        if x == a[i]:
            ids += [i]
    return ids

def search_s(x, a):
    l = a[-1]
    a[-1] = x
    i = 0
    while x != a[i]:
        i += 1
    a[-1] = l
    if i == len(a) - 1 and l != x:
        return None
    else:
        return i

print("Looking for 6:")
print(search_truth(6, lst))
print(search_id(6, lst))
print(search_pos(6, lst))
print(search_s(6, lst))

############# Recherche d'un mot ############
def search_word(w, a):
    for i in range(len(a) - len(w)):
        j = 0
        while j < len(w) and w[j] == a[i + j]:
            j += 1
        if j == len(w):
            return i
    return None

def search_word_sl(w, a):
    for i in range(len(a) - len(w)):
        if w == a[i:i+len(w)]:
            return i
    return None

def search_word_nc(w, a):
    j = 0
    ids = []
    for i in range(len(a)):
        if w[j] == a[i]:
            j += 1
            ids += [i]
            if j == len(w):
                return ids
    return None

print("Looking for [2, 7, 8]:")
print(search_word([2, 7, 8], lst))
print(search_word_sl([2, 7, 8], lst))
print("Looking for [1, 7, 1]:")
print(search_word_nc([1, 7, 1], lst))

############## Recherche dichotomique ############
def search_dico_alea(x, a):
    n = 0
    m = len(a) - 1
    i = randint(n, m)
    while m-n > 1:
        if a[i] == x:
            return i
        elif a[i] < x:
            n = i
        else:
            m = i
        i = (m+n) // 2
    if a[n] == x:
        return n
    elif a[m] == x:
        return m
    else:
        return None

def search_dico(x, a):
    n = 0
    m = len(a) - 1
    while m - n > 1:
        i = (m+n) // 2
        if a[i] == x:
            return i
        elif a[i] < x:
            n = i
        else:
            m = i
    if a[n] == x:
        return n
    elif a[m] == x:
        return m
    else:
        return None

print(search_dico_alea(5, range(30)))
print(search_dico(5, range(30)))

