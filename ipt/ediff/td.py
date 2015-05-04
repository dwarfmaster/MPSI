#!/usr/bin/python3
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# {{{ Exercice 1.1
# F(t, u) = cos(t) - 3u
# F(t, u) = cos(t) + sin(t)*u
# F(t, u) = sqrt(t)*cos(t)/2 + u/(2t)

# TODO
# }}}

# {{{ Exercice 2.1
def Euler(f, t_0, y_0, T, N):
    ys = [y_0]
    t = t_0
    xs = [t]
    h = T/N
    for i in range(1,N+1):
        t += h
        xs += [t]
        ys.append(ys[-1] + h*f(t, ys[-1]))
    return [xs, ys]

def PointMilieu(f, t_0, y_0, T, N):
    t = t_0
    xs = [t]
    ys = [y_0]
    h = T/N
    for i in range(1, N+1):
        t += h
        xs += [t]
        ys.append(ys[-1] + h*f(t+h/2, ys[-1] + h/2 * f(t, ys[-1])))
    return [xs, ys]

def SolvTest(f, t_0, y_0, T, N, solver, title):
    cls = ['red', 'blue', 'cyan', 'black', 'salmon', 'yellow']
    for i in range(len(solver)):
        sol = solver[i](f, t_0, y_0, T, N)
        plt.plot(sol[0], sol[1], label=title[i], color=cls[divmod(i,len(cls))[1]])

    def f2(t, u):
        return f(u, t)
    xs = np.linspace(t_0, t_0+T, 500)
    ys = odeint(f2, y_0, xs)
    plt.plot(xs, ys, label="Odeint", color=(0, 1, 0))
    plt.legend()
    plt.show()

def F(t, u):
    return math.cos(t) - 3*u

# SolvTest(F, 0, 1, 4*math.pi, 100, [Euler], ["euler"])
# SolvTest(F, 0, 0, 4*math.pi, 100, [PointMilieu], ["milieu"])

def SolvEval(f, t_0, y_0, T, N, solver):
    ns = range(10, N)
    def diff(n):
        sol = solver(f, t_0, y_0, T, n)
        xs = sol[0]
        def f2(u, t):
            return f(t, u)
        ys = odeint(f2, y_0, xs)
        return abs(sol[1][-1] - ys[-1])
    dfs = [math.log10(diff(n)) for n in ns]
    xs =  [math.log10(n) for n in ns]
    plt.plot(xs, dfs)
    plt.show()

# SolvEval(F, 0, 0, math.pi, 1000, Euler)
# SolvEval(F, 0, 0, math.pi, 1000, PointMilieu)
def F2(t, u):
    return u
# SolvEval(F2, 0, 1, 1, 1000, Euler)

# Exercice 2.2
def vect_mul(sc, vec):
    return [sc*vc for vc in vec]

def EulerV(f, t_0, y_0, T, N):
    ys = [y_0]
    t = t_0
    xs = [t]
    h = T/N
    for i in range(1,N+1):
        t += h
        xs += [t]
        ys.append(ys[-1] + vect_mul(h, f(t, ys[-1])))
    return [xs, ys]

def F3(t, U):
    return [0.25*U[1] - math.sin(U[0]), U[1]]
# print(EulerV(F3, 0, [1, 0], 4*math.pi, 10))
# }}}

# {{{ Exercice 2.3
def Newton(g, x_0, eps):
    def delta(f, x):
        h = 1e-5
        return (f(x+h) - f(x-h)) / (2*h)
    xn = x_0
    xn1 = -g(xn) / delta(g, xn) + xn
    while abs(xn - xn1) >= eps:
        xn = xn1
        xn1 = -g(xn) / delta(g, xn) + xn
    return xn1

def EulerImplicite(f, t_0, y_0, T, N):
    xs = [t_0]
    h = T/N
    ys = [y_0]
    t = t_0
    for i in range(1, N):
        t += h
        xs.append(t)
        def fi(x):
            return x - h*f(t+h,x) - ys[-1]
        ys.append(Newton(fi, ys[-1], 1e-5))
    return [xs, ys]

# SolvTest(F, 0, 1, 3*math.pi, 20,
#         [EulerImplicite, Euler,   PointMilieu],
#         ["euler_imp",    "euler", "ptmilieu"])
# }}}

# {{{ Exercice 2.5
def solving():
    def F(t, U):
        return [U[1], U[0]*U[0]*U[0] + 1]
    def F2(U, t):
        return F(t, U)
    def f(x):
        return odeint(F2, [1, x], xs)[-1][0] - 2
    xs = np.linspace(0, 1, 500)
    A = np.linspace(-1, 1, 20)
    D = [f(a) for a in A]
    plt.plot(A, D)
    plt.show()

    # TODO
    def dicho(f, a, b):
        e = 0.1
        while b - a >= e:
            x = (b - a) / 2
            y = f(x)
            if y < 0:
                a = x
            else:
                b = x
    return dicho(f, -1, 1)
print(solving())
# }}}
