# Python library for basic matrix manipulation

def swap(m, i1, i2):
    """
    Swaps the contents of the i1 and i2 lines
    """
    if len(m) == 0 or len(m) <= max(i1, i2):
        return
    for i in range(len(m[0])):
        m[i1][i], m[i2][i] = m[i2][i], m[i1][i]

def add(m, l1, n, l2):
    """
    Add n times the contents of the l2 line to the l1 one
    """
    for i in range(len(m[0])):
        m[l1][i] += n*m[l2][i]

def mult(m, l, n):
    """
    Multiply each element of the l line by n
    """
    for i in range(len(m[l])):
        m[l][i] *= n

def read(path):
    """
    Reads a matrix from a file : returns the matrix and a boolean indicating the success
    """
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

def output(m):
    for i in range(len(m)):
        print("| ", end="")
        for j in range(len(m[i])):
            print(repr(m[i][j]).rjust(6), end=" ")
        print("|")


