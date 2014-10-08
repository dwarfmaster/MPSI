#!/usr/bin/python3

def index(s, x):
    for i in range(0, len(s)):
        if x == s[i]:
            return i
    return -1

def list_index(s, x):
    ids = []
    for i in range(0, len(s)):
        if x == s[i]:
            ids += [i]
    return ids

print("Abebdabade")
print(index("Abebdabade", "a"))
print(list_index("Abebdabade", "b"))

