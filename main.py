from os.path import exists

import numpy
import numpy as np
import sys

import dfs
import resolution

sys.setrecursionlimit(1500)


##################################################
# Initialisation

# Writes labyrinth to file
def writeMazeToFile(lab):
    filename = input("Please enter a filename.\n")
    if not exists(filename):
        file = open(filename, "a+")
    else:
        file = open(filename, "w")
    if file.write(lab):
        print("-- Printing complete! --")
    else:
        print("Impossible to write to file", filename, "...")
        writeMazeToFile()
    file.close()


# Initializes labyrinth for printing
def initLabyrinth():
    num = int(input("Please enter labyrinth size between 0 and 50\n"))
    while num <= 0 or num > 50:
        num = int(input("Please enter labyrinth size between 0 and 50\n"))
    size = num * 2 + 1
    labyrinth = np.tile('#', (size, size))
    labyrinth[0][0] = '.'
    labyrinth[1][0] = '.'
    labyrinth[1][1] = '.'
    labyrinth[-1][-1] = '.'
    labyrinth[-2][-1] = '.'
    labyrinth[-2][-2] = '.'
    return labyrinth


# Appends a string to print labyrinth
def printLabyrinth(labyrinth):
    lab = ""
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth)):
            if labyrinth[i][j] == '.':
                lab += '' + labyrinth[i][j] + ''
            else:
                lab += '' + (labyrinth[i][j]) + ''
        lab += '\n'
    return lab


# Initializes visited cell list
def initVisitedCells():
    # Add walls to visited cells list
    cells = []

    # line 0
    for j in range(mazeSize):
        if (0, j) not in cells:
            cells.append((0, j))

    # column 0
    for i in range(mazeSize):
        if (i, 0) not in cells:
            cells.append((i, 0))

    # line mazesize - 1
    for j in range(mazeSize):
        if (mazeSize - 1, j) not in cells:
            cells.append((mazeSize - 1, j))

    # column mazesize - 1
    for i in range(mazeSize):
        if (i, mazeSize - 1) not in cells:
            cells.append((i, mazeSize - 1))

    cells.sort()
    return cells


########################################################
labyrinth = initLabyrinth()
mazeSize = len(labyrinth)
cells = initVisitedCells()

# DFS
path = [
    (1, 1)
]
link = []

print("-- Generating the labyrinth, please wait! --")
dfs.dfs(labyrinth, link, cells, 1, 1)

# Visited cells
# cells.sort()
# print("FINAL Cells:", cells)
# print("len of cells", len(cells))

# Link between cells -> Kruskal
# print("Link between cells:", link)

# Printing the labyrinth
print("Printing labyrinth : ")
lab = printLabyrinth(labyrinth)
print(lab)

# Resolution
# Works on small labyrinth but fails to pop the wrong path on bigger labyrinth
print("Resolution:", path)
print("Len of resolution path", len(path))
res = numpy.copy(labyrinth)

realPath = []
resolution.resolution(path, res, 1, 1, realPath, False, mazeSize)

print("Checking if res checks every cell possible")
print(printLabyrinth(res))

print("Resolution path :", realPath)
