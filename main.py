from os.path import exists
import numpy as np


def init_labyrinth():
    num = int(input("Entrez la taille du labyrinthe\n"))
    size = num * 2 + 1
    labyrinth = np.tile('#', (size, size))
    # labyrinth[i][j] = ' '
    # on creuse le passage petit a petit
    print(labyrinth, "\n")
    return labyrinth


labyrinth = init_labyrinth()


# Return True if tile was visited and False if not

def upTile(tiles, i, j):
    if i != 0:
        if (i - 1, j) in tiles:
            return True
    else:
        return False


def downTile(tiles, i, j):
    if i != len(labyrinth):
        if (i + 1, j) in tiles:
            return True
        else:
            return False


def leftTile(tiles, i, j):
    if j != 0:
        if (i, j - 1) in tiles:
            return True
        else:
            return False


def rightTile(tiles, i, j):
    if j != len(labyrinth):
        if (i, j + 1) in tiles:
            return True
        else:
            return False


# List of visited tiles: exemple for tests
tiles = {(0, 0), (1, 0)}

filename = input("Entrez un nom de fichier\n")
if not exists(filename):
    file = open(filename, "a+")
else:
    file = open(filename, "w")

labyrinth.tofile(file, '', '%s')
file.close()
