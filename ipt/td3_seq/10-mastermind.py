#!/usr/bin/python3

def suppi(l, i):
    return l[0:i] + l[i+1:len(l)]

def suppe(l, r):
    ret = []
    for i in range(0, len(l)):
        if r == l[i]:
            ret += l[i+1:len(l)]
            break
        ret += [l[i]]
    return ret

def reponse(c, e):
    nn = 0
    nb = 0

    i = 0
    while i < len(c):
        if c[i] == e[i]:
            nn += 1
            e = suppi(e, i)
            c = suppi(c, i)
        else:
            i += 1

    i = 0
    while i < len(c):
        if c[i] in e:
            e = suppe(e, c[i])
            c = suppi(c, i)
            nb += 1
        else:
            i += 1

    return [nn, nb]

def test(c, e):
    print(e, "->", reponse(c,e))

if __name__ == "__main__":
    test([0,1,1,2], [3,3,3,3])
    test([0,1,1,2], [1,3,3,3])
    test([0,1,1,2], [3,4,5,1])
    test([0,1,1,2], [2,3,4,5])
    test([0,1,1,2], [1,0,3,3])
    test([0,1,1,2], [1,0,2,3])
    test([0,1,1,2], [1,2,0,1])
    test([0,1,1,2], [3,4,1,5])
    test([0,1,1,2], [3,1,4,1])
    test([0,1,1,2], [1,3,3,2])
    test([0,1,1,2], [2,1,0,1])
    test([0,1,1,2], [0,3,1,4])
    test([0,1,1,2], [2,1,1,3])
    test([0,1,1,2], [1,3,1,2])
    test([0,1,1,2], [2,1,1,0])
    test([0,1,1,2], [1,1,0,2])
    test([0,1,1,2], [0,1,2,2])
    test([0,1,1,2], [0,1,1,1])
    test([0,1,1,2], [1,0,2,1])
    test([0,1,1,2], [1,1,1,1])
    test([0,1,1,2], [0,1,1,2])

