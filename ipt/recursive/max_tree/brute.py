#!/usr/bin/python3

max_sum = 0
max_path = []

# Check the path left and right from the (i,j)
# Will go for p levels
# When p is 0, compare with the highest
def brute(tree, p, s, path, j, i):
    global max_sum
    global max_path

    if p == 0:
        s += tree[j][i]
        if s > max_sum:
            max_sum = s
            max_path = path[:]
        return
    path.append(0)
    brute(tree, p-1, s + tree[j][i], path, j+1, i)
    path[-1] = 1
    brute(tree, p-1, s + tree[j][i], path, j+1, i+1)
    path.pop()

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

if __name__ == "__main__":
    tree = [
            [3],
            [1, 2],
            [4, 5, 6],
            [10, 8, 9, 7]
           ]
    path = []
    brute(tree, len(tree) - 1, 0, path, 0, 0)
    print("Max length :", max_sum)
    ppath(max_path)

