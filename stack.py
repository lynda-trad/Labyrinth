class Stack:
    def __init__(self, *args):
        self = []
        for i in range(len(args)):
            self.push(args[i])

    def push(self, cell):
        self.append(cell)

    def pop(self):
        if len(self) != 0:
            return "Pile vide"
        cell = self[-1]
        del self[-1]
        return cell

