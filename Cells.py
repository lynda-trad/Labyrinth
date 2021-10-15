import numpy as np


def initCellArray(size):
    cellArray = np.empty((size, size), dtype=object)
    index = -1
    for i in range(size):
        for j in range(size):
            index += 1
            cellArray[i][j] = Cells((i, j), index)
    print("Simple print :", cellArray)
    print("printCellArray :")
    printCellArray(cellArray)


def printCellArray(cellArray):
    print("printCellArray test: ")
    for i in range(len(cellArray)):
        for j in range(len(cellArray)):
            print(cellArray[i][j].printCell())


class Cells:
    def __init__(self, coord, index):
        self.char = '#'
        self.coordinates = coord
        self.index = index

    def getCoordinates(self):
        return self.coordinates

    def getIndex(self):
        return self.index

    def getChar(self):
        return self.char

    def setCoordinates(self, coord):
        self.coordinates = coord

    def setIndex(self, index):
        self.index = index

    def setChar(self, char):
        self.char = char

    def printCell(self):
        strCell = ""
        strCell += "Cell index : " + str(self.index) + "\n"
        strCell += "Coordinates : [" + str(self.coordinates[0]) + "," + str(self.coordinates[1]) + "]\n"
        return strCell
