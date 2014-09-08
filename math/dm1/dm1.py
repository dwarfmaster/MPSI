#!/usr/bin/python3

n = 0
ls = [ ]
for n in range(0, 100):
    ls.append(n + 1)

l = 0
for l in range(1, 100):
    for n in range(0, 100-l):
        ls[n] = ls[n] + ls[n+1]
print("Result : ", ls[0])
print("Theo   : ", 2**98 * 101)

