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

filename = input("Entrez un nom de fichier\n")
if not exists(filename):
    file = open(filename, "a+")
else:
    file = open(filename, "w")

labyrinth.tofile(file, '', '%s')
file.close()
