#!/usr/bin/python3

import random as rd;

# The tree
# tree = [
#         [3],
#         [1, 2],
#         [4, 5, 6],
#         [10, 8, 9, 7]
#        ]

# Create a random tree of depth n and print it
def randtree(n):
    tr = [None] * n
    print("Tree :")
    for i in range(n):
        tr[i] = [None] * (i+1)
        for j in range(i+1):
            tr[i][j] = rd.randint(0,500)
        print(tr[i])
    return tr

# Fill tree_l and tree_p to level n, considering n-1 is filled
def fill(tree, tree_l, tree_n, n):
    for i in range(len(tree[n])):
        if i == 0:
            tree_l[n][0] = tree_l[n-1][0] + tree[n][0]
            tree_p[n][0] = tree_p[n-1][0] + [0]
        elif i == n:
            tree_l[n][-1] = tree_l[n-1][-1] + tree[n][-1]
            tree_p[n][-1] = tree_p[n-1][-1] + [1]
        else:
            ll = tree_l[n-1][i-1]
            lr = tree_l[n-1][i]
            if ll > lr:
                tree_l[n][i] = ll + tree[n][i]
                tree_p[n][i] = tree_p[n-1][i-1] + [1]
            else:
                tree_l[n][i] = lr + tree[n][i]
                tree_p[n][i] = tree_p[n-1][i] + [0]

# Create the intermediary lists
def create(tree, tree_l, tree_p):
    for j in range(len(tree)):
        tree_l[j] = [None] * len(tree[j])
        tree_p[j] = [None] * len(tree[j])

# Get the index of the max elem
def maxl(l):
    mid = 0
    mv = l[0]
    for i in range(len(l)):
        if l[i] > mv:
            mv = l[i]
            mid = i
    return mid

# Print path
def ppath(p):
    print(tree[0][0], sep="", end="")
    y = 0
    x = 0
    for i in range(len(p)):
        print(" -> ", sep="", end="")
        y += 1
        if p[i] == 1:
            x += 1
        print(tree[y][x], sep="", end="")
    print("")

# Algorithm
if __name__ == "__main__":
    l = rd.randint(10, 20)
    print("Length :", l)
    tree = randtree(l)
    tree_l = [None]*len(tree)
    tree_p = [None]*len(tree)
    create(tree, tree_l, tree_p)
    tree_l[0][0] = tree[0][0]
    tree_p[0][0] = []
    for i in range(1,len(tree)):
        fill(tree, tree_l, tree_p, i)
    mid = maxl(tree_l[-1])
    print("Max length", tree_l[-1][mid])
    print("Path :", tree_p[-1][mid])
    ppath(tree_p[-1][mid])


