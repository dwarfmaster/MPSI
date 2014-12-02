#!/usr/bin/python3

######### Imports #######
import string

######### Type definition #######
# A matrix is an array of arrays. More precisely, it 
# is an array of lines

######### IO #########
# Returns the matrix and a boolean indicating the success
def input_matrix(x, y):
    mat = []
    for i in range(y):
        print("line", i, end=" : ")
        line = input()
        row  = [int(s.strip()) for s in line.split()]
        if len(row) != x:
            return mat, False
        mat.append(row)
    return mat, True

def output_matrix(m):
    for i in range(len(m)):
        print("|  ", end="")
        for j in range(len(m[i])):
            print(m[i][j], end="  ")
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

######### Main loop ##########
if __name__ == "__main__":
    n = int(input("Enter n : "))
    p = int(input("Enter p : "))
    print("Enter the coeffs :")
    coeffs, b = input_matrix(p, n)
    if not b:
        print("You can't even type a correct matrix !")
        exit()
    print("Enter the second members : ")
    seconds, b = input_matrix(1, n)
    if not b:
        print("You can't even type a correct matrix !")
        exit()

    output_matrix(coeffs)
    print("Appending seconds to coeffs : ")
    matrix_append(coeffs, seconds)
    output_matrix(coeffs)
    print("Swapping line 0 and 1 :")
    matrix_swap(coeffs, 0, 1)
    output_matrix(coeffs)
    print("Soustracting line 1 to line 0 :")
    matrix_add(coeffs, 1, -1, 0)
    output_matrix(coeffs)

