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
    labyrinth[- 1][- 1] = ' '
    labyrinth[- 2][- 1] = ' '
    labyrinth[- 2][- 2] = ' '

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
    # ERROR : cant access tuple and check if Out of bounds bc changed to dictionary
    neighbours = {(i - 1, j): 'up', (i + 1, j): 'down', (i, j - 1): 'left', (i, j + 1): 'right'}
    for tup in neighbours.keys():
        if 0 in tup or -1 in tup:
            neighbours.pop(tup)
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
            path[(x, y)] = neighbours[(x, y)]
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
    (1, 1): []
}
DFS_bis(path, link, 1, 1)
print("Second version of DFS:", path)
print("len of path", len(path))

cells.sort()
print("FINAL Cells:", cells)
print("len of cells", len(cells))

# Arretes entre les cases
print("Link between cells:", link)



# NOTES POUR LA SUITE
# on crée un dictionnaire path qui prend en item
# une cellule (coordonnées) et ses murs qui sont cassés ( maximum 2 puisque verif visited or not)
# exemple :path = ( (1,1): left, right)
# a chaque deplacement de cellule on note la direction prise et
# on lui casse le mur dans le dico path ->
# on fait de meme pour le mur opposé de la case suivante