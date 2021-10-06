import random
from os.path import exists
import numpy as np


def init_labyrinth():
    num = int(input("Entrez la taille du labyrinthe\n"))
    size = num * 2 + 1
    labyrinth = np.tile('#', (size, size))

    # Beginning and end
    labyrinth[0][0] = ' '
    labyrinth[1][0] = ' '
    labyrinth[1][1] = ' '
    labyrinth[size - 1][size - 1] = ' '
    labyrinth[size - 2][size - 1] = ' '
    labyrinth[size - 2][size - 2] = ' '

    # on creuse le passage petit a petit
    print(labyrinth, "\n")
    return labyrinth


labyrinth = init_labyrinth()
mazeSize = len(labyrinth)


# Return True if tile was visited and False if not

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


def findUnvisitedCell(cells, i, j):
    # picks a random direction
    direction = random.randint(0, 3)
    print(direction)
    if direction == 0:
        if not upCell(cells, i, j):
            print("up")
            if i != 0:
                return (i - 1, j)
            else:
                findUnvisitedCell(cells, i, j)
        else:
            findUnvisitedCell(cells, i, j)

    elif direction == 1:
        if not downCell(cells, i, j):
            print("down")
            if i != mazeSize - 1:
                return (i + 1, j)
            else:
                findUnvisitedCell(cells, i, j)
        else:
            findUnvisitedCell(cells, i, j)

    elif direction == 2:
        if not leftCell(cells, i, j):
            print("left")
            if j != 0:
                return (i, j - 1)
            else:
                findUnvisitedCell(cells, i, j)
        else:
            findUnvisitedCell(cells, i, j)

    elif direction == 3:
        if not rightCell(cells, i, j):
            print("right")
            if j != mazeSize - 1:
                return (i, j + 1)
            else:
                findUnvisitedCell(cells, i, j)
        else:
            findUnvisitedCell(cells, i, j)


def writeMazeToFile():
    filename = input("Entrez un nom de fichier\n")
    if not exists(filename):
        file = open(filename, "a+")
    else:
        file = open(filename, "w")
    labyrinth.tofile(file, '', '%s')
    file.close()


# List of visited tiles: start and finish
cells = {
        (0, 0), (1, 0), (1, 1),
        (mazeSize - 1, mazeSize - 1),
        (mazeSize - 2, mazeSize - 2),
        (mazeSize - 2, mazeSize - 1)
        }

# Test findUnvisitedCell with cell 0 0 and cell 1 0
newCell = findUnvisitedCell(cells, 2, 0)
print("Random unvisited adjacent cell of (2,0) is : ", newCell)

newCell = findUnvisitedCell(cells, 2, 0)
print("Random unvisited adjacent cell of (2,0) is : ", newCell)

newCell = findUnvisitedCell(cells, 2, 0)
print("Random unvisited adjacent cell of (2,0) is : ", newCell)

newCell = findUnvisitedCell(cells, mazeSize - 1, 0)
print("Random unvisited adjacent cell of (", mazeSize - 1, ",0) is : ", newCell)
