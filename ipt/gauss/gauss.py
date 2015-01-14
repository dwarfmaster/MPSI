#!/usr/bin/python3

######### Imports #######
import string
import sys
import matrix

######### Type definition #######
# A matrix is an array of arrays. More precisely, it 
# is an array of lines

######### Utilities #########
def is_zero(n):
    return abs(n) < 1e-10

def first_nonzero(l):
    """
    Returns the index of the first non-zero element or len(l) if the array is full of zeros
    """
    for i in range(len(l)):
        if not is_zero(l[i]):
            return i
    return len(l)

######### LaTeX output ########
# The latex file :
latex_file = False

def latex_begin(coeffs, path):
    """
    Open the path file and start writing a solution in it.
    """
    global latex_file
    latex_file = open(path, "wt")
    if not latex_file:
        return False
    latex_file.write("\\begin{figure}\n")
    latex_file.write("\\begin{math}\n")
    latex_matrix(coeffs)
    latex_file.write("\\\\")
    return True

def latex_end(sol):
    """
    End the latex presentation and close the file.
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\end{math}\n")
    if not sol:
        latex_file.write("There is no solution.\n")
    else:
        latex_file.write("The solutions are : \\\\\n")
        latex_file.write("\\begin{equation}\n")

        latex_file.write("\\left(\\begin{array}{c}")
        for j in range(len(sol)):
            latex_file.write("x_{" + "{}".format(j) + "} \\\\ ")
        latex_file.write("\\end{array}\\right)\n \\in")

        latex_file.write("\\left(\\begin{array}{c}")
        for j in range(len(sol)):
            latex_file.write("{} \\\\ ".format(sol[j][0]))
        latex_file.write("\\end{array}\\right) + {\\rm Vect}\\left\\{")

        for i in range(1, len(sol[0])):
            latex_file.write("\\left(\\begin{array}{c}\n")
            for j in range(len(sol)):
                latex_file.write("{} \\\\ ".format(sol[j][i]))
            latex_file.write("\n\\end{array}\\right)\n")

        latex_file.write("\\right\\}\n")
        latex_file.write("\\end{equation}\n")

    latex_file.write("\\caption{Solving a linear system}\n")
    latex_file.write("\\end{figure}\n")
    latex_file.close()
    latex_file = None

def latex_step(m):
    """
    Add an intermediary step to the latex file
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\Leftrightarrow")
    latex_matrix(m)
    latex_file.write("\\\\\n")

def latex_matrix(m):
    """
    Output a matrix in latex format to the latex file.
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\left\\{\\begin{array}{")
    latex_file.write("c" * (2*len(m[0]) - 1))
    latex_file.write("} ")
    for j in range(len(m)):
        for i in range(len(m[j]) - 2):
            latex_elem(m[j][i], i, True)
        latex_elem(m[j][-2], len(m[j]) - 2, False)
        latex_file.write("= & {} \\\\\n".format(m[j][-1]))
    latex_file.write("\\end{array}\\right.")
    return None

def latex_elem(e, i, p):
    """
    Output a single element to the latex_file
    """
    global latex_file
    if is_zero(e):
        latex_file.write("& ")
        if p:
            latex_file.write("& ")
        return False
    elif is_zero(e - 1):
        latex_file.write("x_{" + "{}".format(i) + "} & ")
    elif is_zero(e + 1):
        latex_file.write("-x_{" + "{}".format(i) + "} & ")
    else:
        latex_file.write("{}".format(e) + "x_{" + "{}".format(i) + "} & ")
    if p:
        latex_file.write("+ & ")
    return True

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
            latex_step(m)
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
    latex_begin(coeffs, "latex.matrix")
    print("Triangularized :")
    comp = triangularize(coeffs, p)
    bs = base(p, comp)
    matrix.output(coeffs)
    if not solve(coeffs, bs, p):
        print("No solution.")
        latex_end(None)
    else:
        print("Solution : ")
        output_results(bs)
        latex_end(bs)

