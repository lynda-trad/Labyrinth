from os.path import exists

import numpy
import numpy as np
import sys

import dfs
import resolution

sys.setrecursionlimit(1500)


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

##################################################
# Initialisation


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
    stringLab = ""
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth)):
            if labyrinth[i][j] == '.':
                stringLab += '' + labyrinth[i][j] + ''
            else:
                stringLab += '' + (labyrinth[i][j]) + ''
        stringLab += '\n'
    return stringLab


# Initializes visited cell list
def initVisitedCells():
    # Add walls to visited cells list
    cellsList = []

    # line 0
    for j in range(mazeSize):
        if (0, j) not in cellsList:
            cellsList.append((0, j))

    # column 0
    for i in range(mazeSize):
        if (i, 0) not in cellsList:
            cellsList.append((i, 0))

    # line mazesize - 1
    for j in range(mazeSize):
        if (mazeSize - 1, j) not in cellsList:
            cellsList.append((mazeSize - 1, j))

    # column mazesize - 1
    for i in range(mazeSize):
        if (i, mazeSize - 1) not in cellsList:
            cellsList.append((i, mazeSize - 1))

    cellsList.sort()
    return cellsList


########################################################
labyrinth = initLabyrinth()
mazeSize = len(labyrinth)
cells = initVisitedCells()

# DFS
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
path = [
    (1, 1)
]
endingPath = []
res = numpy.copy(labyrinth)

resolution.resolution(path, res, 1, 1, endingPath, False)

print("Resolution path :", endingPath)
print("Len of resolution path", len(endingPath))

print("Checking if res checks every cell possible")
print(printLabyrinth(res))
