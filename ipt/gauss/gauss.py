#!/usr/bin/python3

######### Imports #######
import string
import sys

######### Type definition #######
# A matrix is an array of arrays. More precisely, it 
# is an array of lines

######### Utilities #########
def is_zero(n):
    return abs(n) < 1e-10

######### IO #########
# Returns the matrix and a boolean indicating the success
def input_matrix(x, y):
    mat = []
    for i in range(y):
        print("line", i, end=" : ")
        line = input()
        row  = [float(s.strip()) for s in line.split()]
        if len(row) != x:
            return mat, False
        mat.append(row)
    return mat, True

# Reads a matrix from a file : returns the matrix and a boolean indicating the success
def read_matrix(path):
    f = open(path, 'r')
    m = []
    if not f:
        return m, False
    x = -1
    for line in f:
        if len(line) == 0 or line[0] == '#':
            continue
        row = [float(s.strip()) for s in line.split()]
        if x < 0:
            x = len(row)
        elif len(row) != x:
            return m, False
        m.append(row)
    return m, True

def output_matrix(m):
    for i in range(len(m)):
        print("| ", end="")
        for j in range(len(m[i])):
            print(repr(m[i][j]).rjust(6), end=" ")
        print("|")

######### Matrix manipulation ########
# Swaps the contents of the i1 and i2 lines
def matrix_swap(m, i1, i2):
    if len(m) == 0 or len(m) <= max(i1, i2):
        return
    for i in range(len(m[0])):
        m[i1][i], m[i2][i] = m[i2][i], m[i1][i]

# Appends the contents of each line of m2 to each line of m1
def matrix_append(m1, m2):
    if len(m1) != len(m2):
        return
    for i in range(len(m1)):
        m1[i].extend(m2[i])

# Add n times the contents of the l2 line to the l1 one
def matrix_add(m, l1, n, l2):
    for i in range(len(m[0])):
        m[l1][i] += n*m[l2][i]

######### Gauss transformation ########
# Remove the x-eme element in lines ]y,end[
# Returns false if it was already removed
def gauss_remove(m, x, y):
    piv = None
    for j in range(y, len(m)):
        if is_zero(m[j][x]):
            continue
        if not piv:
            piv = m[j][x]
            if j != y:
                matrix_swap(m, j, y)
            continue
        matrix_add(m, j, -m[j][x]/piv, y)
    if piv:
        return True
    else:
        return False

# Triangularize the matrix with p coeffs using the
# gauss method
def gauss_trian(m, p):
    j = 0
    for i in range(p):
        if gauss_remove(m, i, j):
            j += 1

######### Main loop ##########
if __name__ == "__main__":
    coeffs, b = read_matrix(sys.argv[1])
    if not b:
        print("Invalid file :", sys.argv[1])
        exit()
    p = len(coeffs) - 1

    output_matrix(coeffs)
    print("Gauss-triangularize :")
    gauss_trian(coeffs, p)
    output_matrix(coeffs)

