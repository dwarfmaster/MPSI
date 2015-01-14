# Python library with miscelaneous utilities

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

