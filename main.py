import random
from os.path import exists
import numpy as np


# Writes labyrinth to file
def writeMazeToFile():
    filename = input("Entrez un nom de fichier\n")
    if not exists(filename):
        file = open(filename, "a+")
    else:
        file = open(filename, "w")
    labyrinth.tofile(file, '', '%s')
    file.close()


# Initializes labyrinth for printing
def init_labyrinth():
    num = int(input("Entrez la taille du labyrinthe\n"))
    size = num * 2 + 1
    labyrinth = np.tile('#', (size, size))

    labyrinth[0][0] = '.'
    labyrinth[1][0] = '.'
    labyrinth[1][1] = '.'
    labyrinth[- 1][- 1] = '.'
    labyrinth[- 2][- 1] = '.'
    labyrinth[- 2][- 2] = '.'

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

    cells.sort()
    return cells


def invertDir(d):
    if d == 'up':
        return 'down'
    if d == 'down':
        return 'up'
    if d == 'left':
        return 'right'
    if d == 'right':
        return 'left'


def get_neighbours(i, j):
    neighbours = {
        'up': (i - 2, j),
        'down': (i + 2, j),
        'left': (i, j - 2),
        'right': (i, j + 2)
    }
    coordinates = [(i - 2, j), (i + 2, j), (i, j - 2), (i, j + 2)]
    for tup in coordinates:
        print("x : ", tup[0], "y: ", tup[1])
        if 0 >= tup[0] or tup[0] >= mazeSize - 1 or 0 >= tup[1] or tup[1] >= mazeSize - 1:
            for key in list(neighbours):
                if neighbours[key] == tup:
                    del neighbours[key]
    return neighbours


def breakableWalls(neighbours, walls, tup, i, j):
    # Adds taken direction to breakable walls
    for key in list(neighbours):
        if neighbours[key] == tup:
            # Current Cell and direction taken
            if (i, j) not in walls:
                walls[(i, j)] = [key]
                return walls
            elif key not in walls[(i, j)]:
                walls[(i, j)].append(key)
                return walls

            # Next Cell and direction inverted
            if tup not in walls:
                walls[tup] = [invertDir(key)]
                return walls
            elif key not in walls[tup]:
                walls[tup].append(invertDir(key))
                return walls


def DFS_bis(path, arretes, walls, i, j):
    cells.append((i, j))
    print("current cell:", (i, j))

    neighbours = get_neighbours(i, j)
    coordinates = []
    for n in neighbours.values():
        coordinates.append(n)
    random.shuffle(coordinates)

    print("neighbours:", neighbours)
    for tup in coordinates:
        if tup not in cells:
            # Add to path
            #print("adds", tup, "to path")
            #print("cells in DFS: BEFORE APPEND", cells)
            path[tup] = tup
            #print("cells in DFS: AFTER APPEND", cells)

            # Adds breakableWalls
            walls = breakableWalls(neighbours, walls, tup, i, j)
            print("Walls", walls)

            # Links between cells for Kruskal later on
            # arretes.append(((i, j), tup))

            # Recursive call
            DFS_bis(path, arretes, walls, tup[0], tup[1])


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

walls = {
    (1, 1): []
}

DFS_bis(path, link, walls, 1, 1)
print("Second version of DFS:", path)
print("len of path", len(path))

cells.sort()
print("FINAL Cells:", cells)
print("len of cells", len(cells))

# Arretes entre les cases
print("Link between cells:", link)

# Breakable Walls
print("Walls:", walls)

# NOTES POUR LA SUITE
# on crée un dictionnaire path qui prend en item
# une cellule (coordonnées) et ses murs qui sont cassés ( maximum 2 puisque verif visited or not)
# exemple :path = ( (1,1): left, right)
# a chaque deplacement de cellule on note la direction prise et
# on lui casse le mur dans le dico path ->
# on fait de meme pour le mur opposé de la case suivante
