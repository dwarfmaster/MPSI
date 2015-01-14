#!/usr/bin/python

import gauss;
import sys;

if __name__ == "__main__":
    # Reading the matrix
    if len(sys.argv) != 2:
        print("Invalid number of arguments : expected 1.")
        exit()
    mat, b = gauss.read_matrix(sys.argv[1])
    if not b:
        print("Invalid file :", sys.argv[1])
        exit()
    if len(mat) != len(mat[0]):
        print("Invalid matrix size : expected a square one.")
        exit()
    gauss.output_matrix(mat)
    print("Inverting ...")

    # Adding identity
    size = len(mat)
    for i in range(len(mat)):
        add = [0] * len(mat)
        add[i] = 1
        mat[i] += add

    # Triangularize
    comp = gauss.triangularize(mat, size)
    if len(comp) != 0:
        print("Can't invert the matrix.")
        exit()

    # Eliminating
    for i in range(len(mat)):
        gauss.matrix_mult(mat, i, 1/mat[i][i])
        for j in range(i):
            gauss.matrix_add(mat, j, -mat[j][i]/mat[i][i], i)

    # Output
    invert = []
    for i in range(len(mat)):
        invert += [[0] * size]
        for j in range(size):
            invert[i][j] = mat[i][j + size]
    gauss.output_matrix(invert)

