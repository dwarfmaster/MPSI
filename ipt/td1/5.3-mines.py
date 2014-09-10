#!/usr/bin/python3

def seq(m):
    n = 0
    sm = 0
    lst = [0]
    j = 1
    while j <= m:
        n = n+1
        sm = sm + 1/n
        if sm >= j:
            j = j+1
            lst = lst + [n]
    return lst

m = 16
elems = seq(m)
for j in range(1,m+1):
    print(j, "=>", elems[j])

print(elems[m]/elems[m-1])

