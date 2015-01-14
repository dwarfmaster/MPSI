#!/usr/bin/python

import sys;
import matrix;
import latex;
from misc import *;

def latex_line(mat):
    p1, p2 = [], []
    size = len(mat)
    for i in range(len(mat)):
        p1 += [[0] * size]
        p2 += [[0] * size]
        for j in range(size):
            p1[i][j] = mat[i][j]
            p2[i][j] = mat[i][j + size]
    latex.matrix(p1)
    latex.output(" & ")
    latex.matrix(p2)
    latex.output(" \\\\")

if __name__ == "__main__":
    # Reading the matrix
    if len(sys.argv) != 2:
        print("Invalid number of arguments : expected 1.")
        exit()
    mat, b = matrix.read(sys.argv[1])
    if not b:
        print("Invalid file :", sys.argv[1])
        exit()
    if len(mat) != len(mat[0]):
        print("Invalid matrix size : expected a square one.")
        exit()
    matrix.output(mat)
    print("Inverting ...")

    # LaTeX output
    latex.begin("latex.matrix")
    latex.beq()
    latex.output("\\begin{array}{cc}\n")

    # Adding identity
    size = len(mat)
    for i in range(len(mat)):
        add = [0] * len(mat)
        add[i] = 1
        mat[i] += add
    latex_line(mat)

    # Eliminating
    for i in range(len(mat)):
        if is_zero(mat[i][i]):
            print("Can't invert the matrix.")
            latex.output("\\end{array}")
            latex.enq()
            latex.output("\\\\Can't invert the matrix.\n")
            latex.end("Inverting the matrix")
            exit()
        matrix.mult(mat, i, 1/mat[i][i])
        for j in range(len(mat)):
            if j == i:
                continue
            matrix.add(mat, j, -mat[j][i], i)
        latex_line(mat)

    # Output
    invert = []
    for i in range(len(mat)):
        invert += [[0] * size]
        for j in range(size):
            invert[i][j] = mat[i][j + size]
    matrix.output(invert)

    # LaTeX output
    latex.output("\\end{array}")
    latex.enq()
    latex.output("\\\\Inverse :\n")
    latex.beq()
    latex.matrix(invert)
    latex.enq()
    latex.end("Inversing a matrix")

