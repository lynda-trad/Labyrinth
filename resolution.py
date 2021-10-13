import random
import sys
import dfs

sys.setrecursionlimit(1500)


##################################################
# Resolution of labyrinth

def resolution(path, res, i, j, realPath, pDone):
    res[i][j] = 'O'  # marks current cell as visited
    print("current cell:", (i, j))

    neighbours = dfs.get_neighbours(i, j, 1, len(res))
    coordinates = []
    for n in neighbours.values():
        coordinates.append(n)
    random.shuffle(coordinates)

    if not pDone:
        resolutionCheck(coordinates, path, res, realPath, pDone)


def resolutionCheck(coordinates, path, res, realPath, pDone):
    for tup in coordinates:
        # if not visited yet '.' & not a wall '#'
        if res[tup[0]][tup[1]] != 'O' and res[tup[0]][tup[1]] == '.':
            # If end cell is reached
            checkEnding(tup, res, len(res), path, realPath, pDone)
            # Add to path
            path.append(tup)
            # Recursive call
            print("Current path:", path)
            print("\nRealpath from outerscope", realPath, '\n')
            resolution(path, res, tup[0], tup[1], realPath, pDone)
        elif popCondition(tup, coordinates, res):
            # Back tracking when you can't move forward anymore
            # ERROR : pop doesnt remove some cells
            if len(path) != 0:
                path.pop(- 1)


def checkEnding(tup, res, mazeSize, path, realPath, pDone):
    print("checkEnding enter")
    if tup == (mazeSize - 2, mazeSize - 2) and not pDone:
        print("checkEnding enter bc NOT DONE")
        res[tup[0]][tup[1]] = 'O'
        print("res change at", tup[0], tup[1], "ok")
        # Copying path into realPath
        for coord in path:
            print("copie des tuples dans realpath")
            realPath.append(coord)
        realPath.append((mazeSize - 2, mazeSize - 2))
        pDone = True
        print(pDone, "after checkEnding bc not done")
        return realPath


def popCondition(tup, coordinates, res):
    first = (res[tup[0]][tup[1]] == 'O' and res[tup[0]][tup[1]] != '.')
    second = (tup == coordinates[len(coordinates) - 1] and tup != (len(res) - 2, len(res) - 2))
    return first and second
