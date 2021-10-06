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
    # picks a random direction
    direction = random.randint(0, 3)
    print("Direction: ", direction)
    if direction == 0:
        print("Direction Up ")
        if upCell(cells, i, j):
            print("Appel a upCell")
            return (i - 1, j)
        else:
            findUnvisitedCell(cells, i, j)
    elif direction == 1:
        print("Direction Down ")
        if downCell(cells, i, j):
            print("Appel a downCell")
            return (i + 1, j)
        else:
            findUnvisitedCell(cells, i, j)
    elif direction == 2:
        print("Direction Left ")
        if leftCell(cells, i, j):
            print("Appel a leftCell")
            return (i, j - 1)
        else:
            findUnvisitedCell(cells, i, j)
    elif direction == 3:
        print("Direction Right ")
        if rightCell(cells, i, j):
            print("Appel a rightCell")
            return (i, j + 1)
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
cells = {(0, 0), (1, 1), (len(labyrinth) - 2, len(labyrinth) - 1), (len(labyrinth) - 1, len(labyrinth) - 1)}

# Test findUnvisitedCell with cell 0 0 and cell 1 0
newCell = findUnvisitedCell(cells, 1, 0)
print("Random unvisited adjacent cell is : ", newCell)

# L'algorithme du parcours en profondeur (ou "recursive backtracker" en anglais) commence sur
# une cellule aléatoire dans le labyrinthe.
# Il suffit ensuite de se diriger dans une direction aléatoire et de casse le mur face
# à soi, tout en marquant la cellule précédente comme visitée.
# Lorsque plus aucune direction n'est disponible, l'algorithme "remonte" à la position
# précédente : c'est le backtracking.
