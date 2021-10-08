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


def writeMazeToFile():
    filename = input("Entrez un nom de fichier\n")
    if not exists(filename):
        file = open(filename, "a+")
    else:
        file = open(filename, "w")
    labyrinth.tofile(file, '', '%s')
    file.close()


# Other version of DFS
def get_neighbours(i, j):
    neighbours = []
    if i != 0:
        neighbours.append((i - 1, j))

    if i != mazeSize - 2:
        neighbours.append((i + 1, j))

    if j != 0:
        neighbours.append((i, j - 1))

    if j != mazeSize - 2:
        neighbours.append((i, j + 1))
    return neighbours


def DFS_bis(path, arretes, i, j):
    cells.append((i, j))
    print("current cell:", (i, j))
    neighbours = get_neighbours(i, j)
    random.shuffle(neighbours)

    print("neighbours:", neighbours)
    for (x, y) in neighbours:
        if (x, y) not in cells:
            print("adds", (x, y), "to path")
            print("cells in DFS: BEFORE APPEND", cells)
            path[(x, y)] = 'path'
            print("cells in DFS: AFTER APPEND", cells)
            arretes.append(((i, j), (x, y)))
            DFS_bis(path, arretes, x, y)
        # elif (x, y) == neighbours[len(neighbours) - 1]:
        # cul de sac
        # path[(i, j)] = 'stop'


########################################################
labyrinth = init_labyrinth()
mazeSize = len(labyrinth)
cells = initVisitedCells()
print("init cells:", cells)


# Second Version of DFS
link = []
path = {
    (1, 1): 'path'
}
DFS_bis(path, link, 1, 1)
print("Second version of DFS:", path)
print("len of path", len(path))

cells.sort()
print("FINAL Cells:", cells)
print("len of cells", len(cells))

# Arretes entre les cases
print("Link between cells:", link)
