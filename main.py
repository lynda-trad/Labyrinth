import string
from os.path import exists
import numpy as np


def init_labyrinth():
    num = int(input("Entrez la taille du labyrinthe\n"))
    size = num * 2 + 1
    labyrinth = np.tile(' ', (size, size))
    for i in range(size):
        labyrinth[0][i] = '#'
    for i in range(size):
        labyrinth[i][0] = '#'
    for i in range(size):
        labyrinth[i][size - 1] = '#'
    for i in range(size):
        labyrinth[size - 1][i] = '#'
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
