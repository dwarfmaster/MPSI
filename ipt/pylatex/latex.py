# Library to output matrix equations to latex
from misc import *;

# The latex file :
latex_file = False

def begin(path):
    """
    Open the path file and start writing a solution in it.
    """
    global latex_file
    latex_file = open(path, "wt")
    if not latex_file:
        return False
    latex_file.write("\\begin{figure}\n")
    return True

def end(caption):
    """
    End the latex presentation and close the file, setting the caption
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\caption{" + caption + "}\n")
    latex_file.write("\\end{figure}\n")
    latex_file.close()
    latex_file = None

def beq():
    """
    Begin math env
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\begin{math}\n")

def enq():
    """
    End math env
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\end{math}\n")

def output(s):
    """
    Output a string to the latex file
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write(s)

def base(sol):
    """
    Output a base to the latex file
    """
    global latex_file
    if not latex_file:
        return
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

def step(m):
    """
    Add an intermediary step to the latex file <=> 'thematrix'
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\Leftrightarrow")
    system(m)
    latex_file.write("\\\\\n")

def system(m):
    """
    Output a system in latex format to the latex file.
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\left\\{\\begin{array}{")
    latex_file.write("c" * (2*len(m[0]) - 1))
    latex_file.write("} ")
    for j in range(len(m)):
        for i in range(len(m[j]) - 2):
            elem(m[j][i], i, True)
        elem(m[j][-2], len(m[j]) - 2, False)
        latex_file.write("= & {} \\\\\n".format(m[j][-1]))
    latex_file.write("\\end{array}\\right.")
    return None

def elem(e, i, p):
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

def matrix(m):
    """
    Output a matrix in latex format to the latex file.
    """
    global latex_file
    if not latex_file:
        return
    latex_file.write("\\left(\\begin{array}{")
    latex_file.write("c" * len(m[0]))
    latex_file.write("}")
    for j in range(len(m)):
        latex_file.write("{} ".format(m[j][0]))
        for i in range(1, len(m[j])):
            latex_file.write("& {} ".format(m[j][i]))
        latex_file.write(" \\\\\n")
    latex_file.write("\\end{array}\\right)")


