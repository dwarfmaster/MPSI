#!/usr/bin/python3

# Return the array of the n-uplets made from the s set
def mults(s, n):
    mlts = []
    if n == 1:
        for e in s:
            mlts.append([e])
        return mlts

    for e in s:
        m = mults(s, n - 1)
        for l in m:
            mlts.append([e] + l)
    return mlts

if __name__ == "__main__":
    s = list("luc")
    print(mults(s, 4))

