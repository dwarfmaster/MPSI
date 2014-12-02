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

######### Main loop ##########
if __name__ == "__main__":
    m, b = input_matrix(4, 4)
    if not b:
        print("You can't even type a correct matrix !")
        exit()
    output_matrix(m)

