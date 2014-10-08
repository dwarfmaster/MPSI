#!/usr/bin/python3

def copie_liste(l, n):
    ret = []
    for i in range(0,n):
        ret += l
    return ret

def copie_ch(s, n):
    return s*n

print(copie_liste([0,1], 5))
print(copie_ch("ab", 5))

