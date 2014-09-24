#!/usr/bin/python3

def oral_bac(L, note_inf = 8, note_sup = 10):
    ret = []
    for i in range(0, len(L)):
        if L[i] >= note_inf and L[i] <= note_sup:
            ret += [i];
    return ret

print(oral_bac([4,5,9,10,7,8]))

