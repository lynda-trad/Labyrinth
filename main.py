import random
from os.path import exists

import numpy
import numpy as np
import sys

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


def invertDirection(d):
    if d == 'up':
        return 'down'
    if d == 'down':
        return 'up'
    if d == 'left':
        return 'right'
    if d == 'right':
        return 'left'


def get_neighbours(i, j, inc):
    neighbours = {
        'up': (i - inc, j),
        'down': (i + inc, j),
        'left': (i, j - inc),
        'right': (i, j + inc)
    }
    coordinates = [(i - inc, j), (i + inc, j), (i, j - inc), (i, j + inc)]
    for tup in coordinates:
        # print("x : ", tup[0], "y: ", tup[1])
        if 0 >= tup[0] or tup[0] >= mazeSize - 1 or 0 >= tup[1] or tup[1] >= mazeSize - 1:
            for key in list(neighbours):
                if neighbours[key] == tup:
                    del neighbours[key]
    return neighbours


def breakableWalls(neighbours, tup, i, j):
    # Adds taken direction to breakable walls
    for key in list(neighbours):
        if neighbours[key] == tup:
            if key == 'up':
                labyrinth[i][j] = '.'  # current cell
                labyrinth[i - 1][j] = '.'  # cell between the neighbours
                labyrinth[tup[0]][tup[1]] = '.'  # next cell
            elif key == 'down':
                labyrinth[i][j] = '.'
                labyrinth[i + 1][j] = '.'
                labyrinth[tup[0]][tup[1]] = '.'
            elif key == 'left':
                labyrinth[i][j] = '.'
                labyrinth[i][j - 1] = '.'
                labyrinth[tup[0]][tup[1]] = '.'
            elif key == 'right':
                labyrinth[i][j] = '.'
                labyrinth[i][j + 1] = '.'
                labyrinth[tup[0]][tup[1]] = '.'
            else:
                print("Error, key is invalid")


def DFS_bis(link, walls, i, j):
    cells.append((i, j))
    # print("current cell:", (i, j))

    neighbours = get_neighbours(i, j, 2)
    coordinates = []
    for n in neighbours.values():
        coordinates.append(n)
    random.shuffle(coordinates)

    # print("neighbours:", neighbours)
    for tup in coordinates:
        if tup not in cells:
            # Breaks walls
            breakableWalls(neighbours, tup, i, j)

            # Links between cells for Kruskal later on
            # link.append(((i, j), tup))

            # Recursive call
            DFS_bis(link, walls, tup[0], tup[1])


def resolution(path, res, i, j, realP, pDone):
    res[i][j] = 'O'  # marks current cell as visited
    print("current cell:", (i, j))

    neighbours = get_neighbours(i, j, 1)
    coordinates = []
    for n in neighbours.values():
        coordinates.append(n)
    random.shuffle(coordinates)

    # if we did not reach the end yet

    for tup in coordinates:
        # not visited yet '.' & not a wall '#'
        if res[tup[0]][tup[1]] != 'O' and res[tup[0]][tup[1]] == '.':
            # If end cell is reached
            if tup == (len(res) - 2, len(res) - 2) and not pDone:
                res[tup[0]][tup[1]] = 'O'
                # Copying path into realPath
                for coord in path:
                    realPath.append(coord)
                realPath.append((len(res) - 2, len(res) - 2))

            # Add to path
            path.append(tup)

            # Recursive call
            print(path)
            print("\nRealpath from outerscope", realP, '\n')
            resolution(path, res, tup[0], tup[1], realP, pDone)
        elif tup == coordinates[len(coordinates) - 1] and res[tup[0]][tup[1]] == 'O' and res[tup[0]][tup[1]] != '.':
            # Back tracking when you can't move forward anymore
            # pop doesnt remove cells at every iteration
            if len(path) != 0:
                path.pop(- 1)


########################################################
labyrinth = initLabyrinth()
mazeSize = len(labyrinth)
cells = initVisitedCells()
# print("init cells:", cells)

# DFS
path = [
    (1, 1)
]
link = []

walls = {
    (1, 1): []
}

print("-- Generating the labyrinth, please wait! --")
DFS_bis(link, walls, 1, 1)

# Visited cells
# cells.sort()
# print("FINAL Cells:", cells)
# print("len of cells", len(cells))

# Link between cells -> Kruskal
# print("Link between cells:", link)

# Breakable Walls
# print("Walls:", walls)

# Printing the labyrinth
print("Printing labyrinth : ")
lab = printLabyrinth(labyrinth)
print(lab)

# Resolution
print("Resolution:", path)
print("Len of resolution path", len(path))
res = numpy.copy(labyrinth)

realPath = []
resolution(path, res, 1, 1, realPath, False)

print("Checking if res checks every cell possible")
print(printLabyrinth(res))

print("Resolution path :", realPath)
