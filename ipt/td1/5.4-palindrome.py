#!/usr/bin/python3

def prepare(chaine):
    """
    Enlève les caractères blancs et met la chaine en minuscule.
    """
    chaine2 = ""
    for l in chaine:
        if l not in {' ', '\n', '\t'}:
            chaine2 = chaine2 + l
    return chaine2.lower()

def palindrome(chaine):
    """
    Indique si la chaine est un palindrome.
    """
    chaine2 = list(prepare(chaine))
    l = len(chaine2)
    for i in range(0, l):
        if chaine2[i] != chaine2[l-i-1]:
            return False
    return True

def longest(chaine):
    """
    Retourne le plus long palindrome trouvé en lisant la chaine dans un sens.
    """
    ch2    = list(prepare(chaine))
    l      = len(ch2)
    pal    = ""
    pallen = 0
    double = False

    for i in range(0, l):
        pl = ""
        pk = l-1
        for j in range(i, l):
            if j > pk:
                break
            elif pallen != 0 and len(pl) + pk - j < pallen:
                break
            for k in range(pk, j, -1):
                if pallen != 0 and len(pl) + k - j < pallen:
                    break
                if ch2[j] == ch2[k]:
                    pl = pl + ch2[j]
                    pk = k - 1
                    break
        if len(pl) > pallen:
            if j != pk:
                pal = pl + ch2[j-1]
                double = True
            else:
                pal = pl
            pallen = len(pal)

    if len(pal) == 0 and len(ch2) > 0:
        return ch2[0]
    elif double:
        return pal + "".join([pal[i] for i in range(len(pal)-2,-1,-1)])
    else:
        return pal + pal[::-1]

def lgstpal(chaine):
    """
    Retourne le plus long palindrome trouvé dans la chaine.
    """
    if palindrome(chaine):
        return chaine
    pal1 = longest(chaine)
    pal2 = longest(chaine[::-1])
    if len(pal1) > len(pal2):
        pal = pal1
    else:
        pal = pal2
    return pal

inp = input("Entrez un phrase : ")
print("Vous avez entré", inp)
pal = lgstpal(inp)
print("Le plus long palindrome trouvé est :", pal)

