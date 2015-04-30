#!/usr/bin/python3
import numpy as np
import random as rd
from math import *
import matplotlib.pyplot as plt

########################################
####### Méthode des rectangles #########
########################################
tests = False

### Exercice 1-a ###
def Irg(f, a, b, n):
    ints = np.linspace(a, b, n + 1)
    summ = 0
    for i in range(len(ints) - 1):
        summ += f(ints[i]) * (ints[i+1] - ints[i])
    return summ

### Exercice 1-b ###
# sin x croissante sur [0; \pi/2] : Irg donne une
# minoration de l'intégrale.
sing = Irg(sin, 0, pi/2, 10)

### Exercice 1-c ###
def Ird(f, a, b, n):
    ints = np.linspace(a, b, n + 1)
    summ = 0
    for i in range(len(ints) - 1):
        summ += f(ints[i+1]) * (ints[i+1] - ints[i])
    return summ

### Exercice 1-d ###
# sin x croissante sur [0; \pi/2] : Ird donne une
# majoration de l'intégrale.
sind = Ird(sin, 0, pi/2, 10)

### Exercice 1-e ###
# On peut considérer que c'est un valeur
# moyenne entre la valeur minimale et la
# valeur maximale : probablement plus
# précise.
sina = .5 * (sind + sing)

### Exercice 2 ###
def Er(meth, f, a, b, n, intex, m1):
    intc = meth(f, a, b, n)
    err = (b-a) * (b-a) / (2*n) * m1
    return abs(intex - intc) <= err

if tests:
    countg = 0
    countd = 0
    for n in range(1, 1001):
        if Er(Irg, sin, 0, pi/2, n, 1, 1):
            countg += 1
        if Er(Ird, sin, 0, pi/2, n, 1, 1):
            countd += 1
    print("Validg : ", countg)
    print("Validd : ", countd)

### Exercice 3-a ###
def Irm(f, a, b, n):
    ints = np.linspace(a, b, n + 1)
    summ = 0
    for i in range(len(ints) - 1):
        summ += f((ints[i] + ints[i+1])/2) * (ints[i+1] - ints[i])
    return summ

### Exercice 3-b ###
def Er2(meth, f, a, b, n, intex, m2):
    intc = meth(f, a, b, n)
    err = (b-a) * (b-a) * (b-a) / (24*n*n) * m2
    return abs(intex - intc) <= err
if tests:
    countm = 0
    for n in range(1, 1001):
        if Er2(Irm, sin, 0, pi/2, n, 1, 1):
            countm += 1
    print("Validm : ", countm)

### Exercice 3-c ###
def f1(x): return x + 2
def f2(x): return x*x
if tests:
    print(Irm(f1, 0, 1, 10))
    print(Irm(f2, 0, 1, 10))

########################################
######## Méthode des trapèzes ##########
########################################
tests = False

### Exercice 1 ###
def It(f, a, b, n):
    ints = np.linspace(a, b, n+1)
    summ = 0
    for i in range(len(ints) - 1):
        summ += (ints[i+1] - ints[i]) * (f(ints[i]) + f(ints[i+1])) / 2
    return summ

### Exercice 2 ###
def Er3(meth, f, a, b, n, intex, m2):
    intc = meth(f, a, b, n)
    err = (b-a) * (b-a) * (b-a) / (12*n*n) * m2
    return abs(intex - intc) <= err
if tests:
    count = 0
    for n in range(1, 1001):
        if Er3(It, sin, 0, pi/2, n, 1, 1):
            count += 1
    print("Valid trap : ", count)

### Exercice 3 ###
if tests:
    print(It(f1, 0, 1, 10))
    print(It(f2, 0, 1, 10))

########################################
######### Méthode de simpson ###########
########################################
tests = False

### Exercice 1 ###
def Isimp(f, a, b, n):
    ints = np.linspace(a, b, n+1)
    summ = 0
    for i in range(len(ints) - 1):
        summ += (ints[i+1] - ints[i]) * (f(ints[i])/6 + 2*f((ints[i]+ints[i+1])/2)/3 + f(ints[i+1])/6)
    return summ

### Exercice 2 ###
def Er4(meth, f, a, b, n, intex, m4):
    intc = meth(f, a, b, n)
    err = (b-a) * (b-a) * (b-a) * (b-a) * (b-a) / (2880*n*n*n*n) * m4
    return abs(intex - intc) <= err
if tests:
    count = 0
    for n in range(1, 1001):
        if Er4(Isimp, sin, 0, pi/2, n, 1, 1):
            count += 1
    print("Valid simp : ", count)

### Exercice 3 ###
def f3(x): return x*x*x
def f4(x): return x*x*x*x
if tests:
    print(Isimp(f3, 0, 1, 10))
    print(Isimp(f4, 0, 1, 10))

########################################
####### Méthode de monte-carlo #########
########################################
tests = False
def Imont(f, a, b, m, n):
    count = 0
    for i in range(n):
        x = rd.uniform(a, b)
        y = rd.uniform(0, m)
        if y < f(x):
            count += 1
    return m * (b-a) * count / n

def f(x): return sqrt(1 - x*x)
if tests:
    mpi = 4 * Imont(f, 0, 1, 1, 1000000)
    print(mpi)

########################################
########## Graphes d'erreur ############
########################################
tests = True

def plotfn(f, a, b, n, cl = 'blue', lb = ''):
    xs = np.linspace(a, b, n)
    ys = [f(x) for x in xs]
    plt.plot(xs, ys, linewidth = 1, color = cl)
    plt.text(xs[-1], ys[-1], lb)

def createfn(m, p):
    return lambda x: m*x + p

def calcerr(meth, f, a, b, n, intex):
    return log(abs(meth(f, a, b, n) - intex))

def errgraph(mts, f, a, b, n, intex, l):
    N = 100
    for m in l:
        plotfn(createfn(-m, 0), 0, log(n), N, 'red', str(-m))

    i = 0
    cls = ['blue', 'green', 'orange', 'salmon', 'cyan']
    my = 0
    for m in mts:
        meth = m[0]
        ys = [calcerr(meth, f, a, b, i, intex) for i in range(1, n+1)]
        xs = [log(i) for i in range(1, n+1)]
        plt.plot(xs, ys, linewidth = 2, color = cls[i])
        plt.text(xs[-1], ys[-1], m[1])
        i = divmod(i+1, len(cls))[1]
        my = max(my, ys[0])

    plt.title("Error graph")
    plt.axis([0, log(n), ys[-1] - 1, my])
    plt.show()

if tests:
     errgraph([[Ird,"ird"], [Irm,"irm"], [It,"trap"], [Isimp, "simp"]],
             sin, 0, pi/2, 1000, 1, [.5, 1, 2, 4])
