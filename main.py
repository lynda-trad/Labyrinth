import random
from os.path import exists
import numpy as np


# Writes labyrinth to file
def writeMazeToFile(lab):
    filename = input("Entrez un nom de fichier\n")
    if not exists(filename):
        file = open(filename, "a+")
    else:
        file = open(filename, "w")
    # Numpy to file
    labyrinth.tofile(file, '', '%s')
    # Print lab to file
    file.write(lab)
    file.close()


# Initializes labyrinth for printing
def initLabyrinth():
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


def printLabyrinth(labyrinth):
    lab = ""
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth)):
            if labyrinth[i][j] == '.':
                lab += ' ' + labyrinth[i][j] + ' '
            else:
                lab += '' + (labyrinth[i][j]) + ''
        lab += '\n'
    return lab


# Initializes visited cell list
def initVisitedCells():
    # Add walls to visited cells list
    cells = []

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

            if key == 'up':
                labyrinth[i][j] = '.'  # current cell
                labyrinth[i - 1][j] = '.'  # cell between the neighbours
                labyrinth[tup[0]][tup[1]] = '.'  # next cell
            elif key == 'down':
                labyrinth[i][j] = '.'  # current cell
                labyrinth[i + 1][j] = '.'  # cell between the neighbours
                labyrinth[tup[0]][tup[1]] = '.'  # next cell
            elif key == 'left':
                labyrinth[i][j] = '.'  # current cell
                labyrinth[i][j - 1] = '.'  # cell between the neighbours
                labyrinth[tup[0]][tup[1]] = '.'  # next cell
            elif key == 'right':
                labyrinth[i][j] = '.'  # current cell
                labyrinth[i][j + 1] = '.'  # cell between the neighbours
                labyrinth[tup[0]][tup[1]] = '.'  # next cell

            # List of breakable walls
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
            path[tup] = tup

            # Adds breakableWalls
            walls = breakableWalls(neighbours, walls, tup, i, j)
            print("Walls", walls)

            # Links between cells for Kruskal later on
            # arretes.append(((i, j), tup))

            # Recursive call
            DFS_bis(path, arretes, walls, tup[0], tup[1])


########################################################
labyrinth = initLabyrinth()
mazeSize = len(labyrinth)
cells = initVisitedCells()
print("init cells:", cells)

# DFS
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

# Visited cells
cells.sort()
print("FINAL Cells:", cells)
print("len of cells", len(cells))

# Link between cells -> Kruskal
print("Link between cells:", link)

# Breakable Walls
print("Walls:", walls)

# Printing the labyrinth
print("Function printLabyrinth : ")
lab = printLabyrinth(labyrinth)
print(lab)

print("Labyrinth:\n", labyrinth)

# Printing to file
writeMazeToFile(lab)
