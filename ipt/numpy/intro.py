#!/usr/bin/python3
from math import *
import matplotlib.pyplot as plt
import numpy as np

def r(p, e, th0, th):
    r = p/(1+e*cos(th-th0))
    return r

def ellipse(p, e, th0, cl):
    t_theta = np.linspace(0, 2*pi, 1000)
    x = [r(p, e, th0, theta) * cos(theta) for theta in t_theta]
    y = [r(p, e, th0, theta) * sin(theta) for theta in t_theta]
    plt.plot(x, y, linewidth = 1, color = cl)
    return

p = 1
e = 0.9
th0 = pi/8

cls = ['red', 'green', 'blue', 'purple', 'orange']
ths = np.linspace(0, 2*pi, 26)
for i in range(len(ths) - 1):
    ellipse(p, e, ths[i], cls[i % len(cls)])

plt.title("Ellipse")
plt.axis("equal")
plt.savefig("Ellipse.pdf")
plt.show()

