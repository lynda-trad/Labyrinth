import random
import sys
import dfs

sys.setrecursionlimit(1500)


##################################################
# Resolution

def resolution(path, res, i, j, realPath, pDone):
    res[i][j] = 'O'  # marks current cell as visited
    mazeSize = len(res)
    print("current cell:", (i, j))

    neighbours = dfs.get_neighbours(i, j, 1, mazeSize)
    coordinates = []
    for n in neighbours.values():
        coordinates.append(n)
    random.shuffle(coordinates)

    for tup in coordinates:
        # not visited yet '.' & not a wall '#'
        if res[tup[0]][tup[1]] != 'O' and res[tup[0]][tup[1]] == '.':
            # If end cell is reached
            if tup == (mazeSize - 2, mazeSize - 2) and not pDone:
                res[tup[0]][tup[1]] = 'O'
                # Copying path into realPath
                for coord in path:
                    realPath.append(coord)
                realPath.append(mazeSize - 2, mazeSize - 2)

            # Add to path
            path.append(tup)

            # Recursive call
            print(path)
            resolution(path, res, tup[0], tup[1], realPath, pDone)
        elif popCondition(tup, coordinates, res):
            # Back tracking when you can't move forward anymore
            # ERROR : pop doesnt remove some cells
            if len(path) != 0:
                path.pop(- 1)


def popCondition(tup, coordinates, res):
    first = (res[tup[0]][tup[1]] == 'O' and res[tup[0]][tup[1]] != '.')
    second = (tup == coordinates[len(coordinates) - 1] and tup != (len(res) - 2, len(res) - 2))
    return first and second

