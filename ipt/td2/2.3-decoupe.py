#!/usr/bin/python3

def decoupe(ch):
    w = ""
    ret = []
    for l in ch:
        if l in {' ', '\n', '\t'}:
            ret += [w]
            w = ""
        else:
            w += l
    if len(w) > 0:
        ret += [w]
    return ret

def decoupe2(ch, nb_caract = 8):
    w = ""
    ret = []
    for l in ch:
        if l in {' ', '\n', '\t'}:
            if len(w) > nb_caract:
                ret += ['-']
            else:
                ret += [w]
            w = ""
        else:
            w += l
    if len(w) > 0:
        ret += [w]
    return ret

def reconstitue(wl):
    line = ""
    for w in wl:
        if len(line) > 0:
            line = line + " " + w;
        else:
            line = w
    return line

wl = decoupe("Hello world, I'm so awesomly strong !")
print(wl)
print(decoupe2("Hello world, I'm so unbilivably strong !", 5))
print(reconstitue(wl))

