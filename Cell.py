class Cell(object):
    def __init__(self, visited, index, position):
        self.visited = False   # is visited or not
        self.neighbours = []   # array of tuples/coordinates
        self.index = 0         # index
        self.position = (0, 0) # coordinates
        self.walls = {"up": False, "down": False, "right": False, "left": False}

    def init_cells(self):
        # tableau de cellule
        labyrinth = [Cell(True, 0, (0, 0)), Cell(True, 0, (0, 1))]



