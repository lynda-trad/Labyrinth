# OLD CODE
import random
from os.path import exists
import numpy as np


# Initializes labyrinth for printing
def init_labyrinth():
    num = int(input("Entrez la taille du labyrinthe\n"))
    size = num * 2 + 1
    labyrinth = np.tile('#', (size, size))

    labyrinth[0][0] = ' '
    labyrinth[1][0] = ' '
    labyrinth[1][1] = ' '
    labyrinth[size - 1][size - 1] = ' '
    labyrinth[size - 2][size - 1] = ' '
    labyrinth[size - 2][size - 2] = ' '

    print(labyrinth, "\n")
    return labyrinth


# Initializes visited cell list
def initVisitedCells():
    # Add walls to visited cells list
    cells = [
        (1, 1),
        (mazeSize - 2, mazeSize - 2)
    ]

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

    print("Visited cells initialisation:", cells, "\n")
    cells.sort()
    return cells


# Returns True if tile was visited and False if not
def upCell(cells, i, j):
    if i != 0:
        if (i - 1, j) in cells:
            return True
    return False


def downCell(cells, i, j):
    if i != mazeSize - 1:
        if (i + 1, j) in cells:
            return True
    return False


def leftCell(cells, i, j):
    if j != 0:
        if (i, j - 1) in cells:
            return True
    return False


def rightCell(cells, i, j):
    if j != mazeSize - 1:
        if (i, j + 1) in cells:
            return True
    return False


# Calls Cell function to check each direction
def upDirection(cells, i, j, directions, randomDir):
    if not upCell(cells, i, j):
        print("up")
        if i != 0:
            print("return up")
            return (i - 1, j)
        else:
            directions.remove(randomDir)
            return findUnvisitedCell(cells, i, j, directions)
    else:
        directions.remove(randomDir)
        return findUnvisitedCell(cells, i, j, directions)


def downDirection(cells, i, j, directions, randomDir):
    if not downCell(cells, i, j):
        print("down")
        if i != mazeSize - 1:
            print("return down")
            return (i + 1, j)
        else:
            directions.remove(randomDir)
            return findUnvisitedCell(cells, i, j, directions)
    else:
        directions.remove(randomDir)
        return findUnvisitedCell(cells, i, j, directions)


def leftDirection(cells, i, j, directions, randomDir):
    if not leftCell(cells, i, j):
        print("left")
        if j != 0:
            print("return left")
            return (i, j - 1)
        else:
            directions.remove(randomDir)
            return findUnvisitedCell(cells, i, j, directions)
    else:
        directions.remove(randomDir)
        return findUnvisitedCell(cells, i, j, directions)


def rightDirection(cells, i, j, directions, randomDir):
    if not rightCell(cells, i, j):
        print("right")
        if j != mazeSize - 1:
            print("return right")
            return (i, j + 1)
        else:
            directions.remove(randomDir)
            return findUnvisitedCell(cells, i, j, directions)
    else:
        directions.remove(randomDir)
        return findUnvisitedCell(cells, i, j, directions)


# Finds first unvisited cell around og cell
def findUnvisitedCell(cells, i, j, directions):
    # picks a random direction
    if len(directions) != 0:
        randomDir = random.choice(directions)
    else:  # if cell is surrounded with visited cells, returns itself
        return (i, j)
    print("Random direction: ", randomDir)
    print("Possible directions : ", directions)

    if randomDir == 0:
        return upDirection(cells, i, j, directions, randomDir)

    elif randomDir == 1:
        return downDirection(cells, i, j, directions, randomDir)

    elif randomDir == 2:
        return leftDirection(cells, i, j, directions, randomDir)

    elif randomDir == 3:
        return rightDirection(cells, i, j, directions, randomDir)


# Depth First Search
def DFS(cells, path, i, j, directions, cellsNumber):
    print("path in DFS:", path)
    newCell = findUnvisitedCell(cells, i, j, directions)
    directions = [0, 1, 2, 3]
    # tant quil reste des cases non visitées on continue le parcours en profondeur
    while cellsNumber != 0:
        if newCell == (i, j):
            if len(path) != 0:
                newCell = path.pop()
                DFS(cells, path, newCell[0], newCell[1], directions, cellsNumber)
            else:
                return path
        path.append(newCell)
        cells.append(newCell)
        cellsNumber -= 1
        DFS(cells, path, newCell[0], newCell[1], directions, cellsNumber)
    return path


########################################################
labyrinth = init_labyrinth()
mazeSize = len(labyrinth)
cells = initVisitedCells()
print("init cells:", cells)

# Test findUnvisitedCell with cell 0 0 and cell 1 0
directions = [0, 1, 2, 3]
# print("\nTest of findUnvisitedCell")
# newCell = findUnvisitedCell(cells, 1, 1, directions)

# Depth First Search
# Starts at cell (1,1)
print("\nTest of Depth First Search")

# First Version of DFS
cellsNumber = mazeSize ^ 2 - (mazeSize * 4 + 2)
path = [(1, 1)]
path = DFS(cells, path, 1, 1, directions, cellsNumber)
print("First version of DFS:", path)
print(cells)