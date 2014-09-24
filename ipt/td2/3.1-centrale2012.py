#!/usr/bin/python3

def nb_chiffres(n, a):
    count = 0
    r = n % 10
    while r == a:
        count += 1
        n //= 10
        r = n % 10
    return count

u = 9
for i in range(1, 14):
    u = 4*u**3 + 3*u**4
    print(i, nb_chiffres(u, 9))

