from os.path import exists

import numpy
import sys

import dfs
import resolution
import draw
import Cells

sys.setrecursionlimit(2500)


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
    while True:
        try:
            num = int(input("Please enter labyrinth size between 1 and 30\n"))
            if int(num) <= 0 or int(num) > 30:
                continue
            break
        except ValueError:
            print("Please input integer only.")
            continue

    size = num * 2 + 1
    labyrinth = numpy.tile('#', (size, size))
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
            stringLab += '' + str(labyrinth[i][j]) + ''
        stringLab += '\n'
    return stringLab


# Prints solution path onto the resolution numpy
def printSolutionPath(res, realPath):
    res[0][0] = res[1][0] = res[1][1] = res[-1][-1] = res[-2][-1] = res[-2][-2] = 'o'
    for i in range(len(res)):
        for j in range(len(res)):
            if (i, j) in realPath:
                res[i][j] = 'o'


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
link = numpy.zeros((mazeSize * mazeSize, mazeSize * mazeSize))

print("-- Generating the labyrinth, please wait! --")
dfs.dfs(labyrinth, link, cells, 1, 1)

# Link between cells -> Kruskal
print("Link between cells:\n", link)

# Printing the labyrinth
print("Printing labyrinth : ")
lab = printLabyrinth(labyrinth)
print(lab)

# Resolution
path = [
    (1, 1)
]
printPath = [
    (1, 1)
]
endingPath = []
res = numpy.copy(labyrinth)

resolution.resolution(path, res, 1, 1, endingPath, False, printPath)

print("Resolution path :", endingPath)
print("Len of resolution path", len(endingPath))

print("Checking if res checks every cell possible")
print(printLabyrinth(res))

# Printing solution path
print("Solution path: ")
res = numpy.copy(labyrinth)
printSolutionPath(res, endingPath)
print(printLabyrinth(res))

# Cells.initCellArray(mazeSize)

# print("Link between cells:\n")
# printLabyrinth(link)

# Write solution to file
# writeMazeToFile(printLabyrinth(res))

# Print labyrinth to png
draw.rectangle("labyrinth.png", res, endingPath, printPath)
