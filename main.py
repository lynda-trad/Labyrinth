from os.path import exists
import numpy as np


def init_labyrinth():
    num = int(input("Entrez la taille du labyrinthe\n"))
    size = num * 2 + 1
    labyrinth = np.tile('#', (size, size))

    # Beginning and end
    labyrinth[0][0] = ' '
    labyrinth[size - 1][size - 1] = ' '

    # on creuse le passage petit a petit
    print(labyrinth, "\n")
    return labyrinth


labyrinth = init_labyrinth()


# Return True if tile was visited and False if not

def upCell(cells, i, j):
    if i != 0:
        if (i - 1, j) in cells:
            return True
    else:
        return False


def downCell(cells, i, j):
    if i != len(labyrinth):
        if (i + 1, j) in cells:
            return True
        else:
            return False


def leftCell(cells, i, j):
    if j != 0:
        if (i, j - 1) in cells:
            return True
        else:
            return False


def rightCell(cells, i, j):
    if j != len(labyrinth):
        if (i, j + 1) in cells:
            return True
        else:
            return False


def findUnvisitedCell(cells, i, j):
    if upCell(cells, i, j):
        return (i - 1, j)
    elif downCell(cells, i, j):
        return (i + 1, j)
    elif leftCell(cells, i, j):
        return (i, j - 1)
    elif rightCell(cells, i, j):
        return (i, j + 1)


# List of visited tiles: start and finish
cells = {(0, 0), (1, 0), (len(labyrinth) - 1, len(labyrinth) - 1)}

# Test findUnvisitedCell with cell 0 0 and cell 1 0
newCell = findUnvisitedCell(cells, 0, 0)
# newCell = findUnvisitedCell(cells, cells[0][0], cells[0][1])
print("Random unvisited adjacent cell is : ", newCell)

filename = input("Entrez un nom de fichier\n")
if not exists(filename):
    file = open(filename, "a+")
else:
    file = open(filename, "w")

labyrinth.tofile(file, '', '%s')
file.close()
