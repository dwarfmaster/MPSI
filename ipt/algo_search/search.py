#!/usr/bin/python3

def search_linearf(a, x):
    """
    Returns the index of x in a if present, None elsewhere.
    """
    for i in range(len(a)):
        if a[i] == x:
            return i
    return None

def search_linearw(a, x):
    """
    Returns the index of x in a if present, None elsewhere.
    """
    i = 0
    while i < len(a) and a[i] != x:
        i += 1
    if i == len(a):
        return None
    else:
        return i

def search_linears(a, x):
    """
    Returns the index of x in a if present, None elsewhere.
    """
    d = a[-1]
    a[-1] = x
    i = 0

    while a[i] != x:
        i += 1

    a[-1] = d
    if i == len(a) - 1 and d != x:
        return None
    else:
        return i

def search_sub(a, m):
    """
    Returns the index of the first inclusion of the sublist m in a. Returns
    None if m is not in a.
    """

    j = 0
    for i in range(len(a)):
        if a[i] != m[j]:
            j = 0
        else:
            j += 1
            if j == len(m):
                return i - len(m) + 1
    return None

def search_dico(a, x):
    """
    Returns the index of x in a if present, None elsewhere.
    """
    mn = 0
    mx = len(a) - 1
    i = 0

    while mx - mn > 1:
        i = (mn + mx) // 2
        if a[i] == x:
            return i
        elif x > a[i]:
            mn = i
        else:
            mx = i
    if a[mn] == x:
        return mn
    elif a[mx] == x:
        return mx
    else:
        return None

x = int(input("Searching : "))
lst = list(range(0,50))
print(search_linearf(lst, x))
print(search_linearw(lst, x))
print(search_linears(lst, x))
print(search_dico(lst, x))

print(search_sub(lst, [6, 7]))

