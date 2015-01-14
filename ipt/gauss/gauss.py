#!/usr/bin/python3

######### Imports #######
import string
import sys
import matrix
import latex
from misc import *;

######### Type definition #######
# A matrix is an array of arrays. More precisely, it 
# is an array of lines

######### IO #########
def output_results(m):
    """
    Print results
    """
    for i in range(len(m)):
        print("|", end="")
        print(repr(m[i][0]).rjust(6), end="")
        print(" |", end="")
        if len(m[i]) == 1:
            print("")
            continue
        if i == int(len(m)/2):
            print(" + Vect ", end="")
        else:
            print("        ", end="")
        print("|", end="")
        for j in range(1, len(m[i])):
            print(repr(m[i][j]).rjust(6), end=" ")
        print("|")

######### Gauss transformation ########
def remove(m, x, y):
    """
    Remove the x-eme element in lines ]y,end[
    Returns false if it was already removed
    """
    piv = None
    for j in range(y, len(m)):
        if is_zero(m[j][x]):
            continue
        if not piv:
            piv = m[j][x]
            if j != y:
                matrix.swap(m, j, y)
            continue
        matrix.add(m, j, -m[j][x]/piv, y)
    if piv:
        return True
    else:
        return False

def triangularize(m, p):
    """
    Triangularize the matrix with p coeffs using the gauss method
    Returns the list of the complementary vars
    """
    j = 0
    comp = []
    for i in range(p):
        if remove(m, i, j):
            j += 1
            latex.step(m)
        else:
            comp += [i]
    return comp

def base(p, comp):
    """
    Create a base for p variables, comp being the array of the complementary variables
    """
    ret = []
    for l in range(p):
        ret.append((len(comp) + 1) * [0.0])
    for i in range(len(comp)):
        ret[comp[i]][i+1] = 1.0
    return ret

def solve(m, bs, p):
    """
    Solve a triangularized linear system, writing the solutions to bs, p being the number of variables.
    Returns False if there are no solutions.
    """
    for i in range(len(m) - 1, -1, -1):
        z = first_nonzero(m[i])
        if z > p:
            continue
        elif z == p:
            return False
        bs[z][0] = m[i][p]
        for j in range(z+1, p):
            matrix.add(bs, z, -m[i][j], j)
        matrix.mult(bs, z, 1.0/m[i][z])
    return True

######### Main loop ##########
if __name__ == "__main__":
    coeffs, b = matrix.read(sys.argv[1])
    if not b:
        print("Invalid file :", sys.argv[1])
        exit()
    p = len(coeffs[0]) - 1

    print("Solving :")
    matrix.output(coeffs)
    latex.begin("latex.matrix")
    latex.beq()
    latex.matrix(coeffs)
    latex.output("\\\\")

    print("Triangularized :")
    comp = triangularize(coeffs, p)
    bs = base(p, comp)
    matrix.output(coeffs)
    latex.enq()
    if not solve(coeffs, bs, p):
        print("No solution.")
        latex.string("No solution.\n")
    else:
        print("Solution : ")
        output_results(bs)
        latex.base(bs)
    latex.end("Solving a linear system")

