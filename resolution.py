import random
import sys
import dfs

sys.setrecursionlimit(1500)


##################################################
# Resolution of labyrinth

def resolution(path, res, i, j, realPath, pDone, printPath):
    res[i][j] = 'o'  # marks current cell as visited

    neighbours = dfs.get_neighbours(i, j, 1, len(res))
    coordinates = []
    for n in neighbours.values():
        coordinates.append(n)
    random.shuffle(coordinates)

    if not pDone:
        resolutionCheck(coordinates, path, res, realPath, pDone, printPath)


def resolutionCheck(coordinates, path, res, realPath, pDone, printPath):
    for tup in coordinates:
        # if not visited yet '.' & not a wall '#'
        if res[tup[0]][tup[1]] != 'O' and res[tup[0]][tup[1]] == '.':
            # If end cell is reached
            checkEnding(tup, res, len(res), path, realPath, pDone)
            # Add to path
            path.append(tup)
            printPath.append(tup)
            # Recursive call
            resolution(path, res, tup[0], tup[1], realPath, pDone, printPath)
            path.pop(- 1)


def checkEnding(tup, res, mazeSize, path, realPath, pDone):
    if tup == (mazeSize - 2, mazeSize - 2) and not pDone:
        res[tup[0]][tup[1]] = 'O'
        # Copying path into realPath
        for coord in path:
            realPath.append(coord)
        realPath.append((mazeSize - 2, mazeSize - 2))
        pDone = True
        return realPath
