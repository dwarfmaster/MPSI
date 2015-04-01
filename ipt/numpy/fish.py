#!/usr/bin/python3
from math import *
import matplotlib.pyplot as plt
import numpy as np

x = [-1,  1, -1]
y = [ 0,  0,  2]
plt.plot(x,y, linewidth = 1, color = 'blue')
x = [-1, 1]
y = [ 0, 2]
plt.plot(x,y, linewidth = 1, color = 'blue')

def circle(xc, yc, r):
    xs = np.linspace(xc - r, xc + r, 100)
    ys = [sqrt(r*r - (x-xc)*(x-xc)) + yc for x in xs]
    plt.plot(xs, ys, linewidth = 1, color = 'blue')
circle(0, 2, 1)

plt.title("fish")
plt.axis("equal")
plt.savefig("fish.pdf")
plt.show()

