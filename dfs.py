import random
import sys

sys.setrecursionlimit(1500)


##################################################
# DFS of labyrinth

# Invert the direction in parameter
def invertDirection(d):
    if d == 'up':
        return 'down'
    if d == 'down':
        return 'up'
    if d == 'left':
        return 'right'
    if d == 'right':
        return 'left'


# Sends array of coordinates of cell's available neighbours
def get_neighbours(i, j, inc, mazeSize):
    neighbours = {
        'up': (i - inc, j),
        'down': (i + inc, j),
        'left': (i, j - inc),
        'right': (i, j + inc)
    }
    coordinates = [(i - inc, j), (i + inc, j), (i, j - inc), (i, j + inc)]
    for tup in coordinates:
        if 0 >= tup[0] or tup[0] >= mazeSize - 1 or 0 >= tup[1] or tup[1] >= mazeSize - 1:
            for key in list(neighbours):
                if neighbours[key] == tup:
                    del neighbours[key]
    return neighbours


# Defines which cells are broken walls and cells in labyrinth numpy array
def breakableWalls(labyrinth, neighbours, tup, i, j):
    # Adds taken direction to breakable walls
    for key in list(neighbours):
        if neighbours[key] == tup:
            if key == 'up':
                labyrinth[i][j] = '.'  # current cell
                labyrinth[i - 1][j] = '.'  # cell between the neighbours
                labyrinth[tup[0]][tup[1]] = '.'  # next cell
            elif key == 'down':
                labyrinth[i][j] = '.'
                labyrinth[i + 1][j] = '.'
                labyrinth[tup[0]][tup[1]] = '.'
            elif key == 'left':
                labyrinth[i][j] = '.'
                labyrinth[i][j - 1] = '.'
                labyrinth[tup[0]][tup[1]] = '.'
            elif key == 'right':
                labyrinth[i][j] = '.'
                labyrinth[i][j + 1] = '.'
                labyrinth[tup[0]][tup[1]] = '.'
            else:
                print("Error, key is invalid")


def dfs(labyrinth, link, cells, i, j):
    cells.append((i, j))

    neighbours = get_neighbours(i, j, 2, len(labyrinth))
    coordinates = []
    for n in neighbours.values():
        coordinates.append(n)
    random.shuffle(coordinates)

    for tup in coordinates:
        if tup not in cells:
            # Breaks walls
            breakableWalls(labyrinth, neighbours, tup, i, j)

            # Links between cells for Kruskal later on
            # size = len(labyrinth)
            # idFirst = size * i + j
            # idSecond = size * tup[0] + tup[1]
            # link[idFirst][idSecond] = 1
            # A link exists between cell idFirst and idSecond

            # Recursive call
            dfs(labyrinth, link, cells, tup[0], tup[1])

######################
# Each cell has an ID :
# the ID is equal to size * x + y
# This way we will make a matrice in which will put
# 1 if two cells are linked by a wall
# default is 0
