import random
import os
import time

class Cell:
    def __init__(self, state=False):
        self.state = state
        self.neighbour = 0

    def __str__(self):
        return 'O ' if self.state else '  '

class Universe:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cells = tuple([tuple([Cell(random.choice((False, True)))
            for i in range(col)]) for i in range(row)])

    def show(self):
        for row in self.cells:
            for cell in row:
                print(cell, end='')
            print()

    def evolve(self):
        self._calc_neighbour()
        self._calc_state()

    def _calc_neighbour(self):
        cells = self.cells
        row = self.row
        col = self.col
        for y in range(row):
            for x in range(col):
                if cells[y - 1][x - 1].state:
                    cells[y][x].neighbour += 1
                if cells[y - 1][x].state:
                    cells[y][x].neighbour += 1
                if cells[y - 1][(x + 1) % col].state:
                    cells[y][x].neighbour += 1
                if cells[y][x - 1].state:
                    cells[y][x].neighbour += 1
                if cells[y][(x + 1) % col].state:
                    cells[y][x].neighbour += 1
                if cells[(y + 1) % row][x - 1].state:
                    cells[y][x].neighbour += 1
                if cells[(y + 1) % row][x].state:
                    cells[y][x].neighbour += 1
                if cells[(y + 1) % row][(x + 1) % col].state:
                    cells[y][x].neighbour += 1

    def _calc_state(self):
        cells = self.cells
        for y in range(self.row):
            for x in range(self.col):
                if cells[y][x].state:
                    if cells[y][x].neighbour not in (2, 3):
                        cells[y][x].state = False
                else:
                    if cells[y][x].neighbour == 3:
                        cells[y][x].state = True
                cells[y][x].neighbour = 0

if __name__ == '__main__':
    os.system('clear')
    u = Universe(24, 40)
    while True:
        u.show()
        u.evolve()
        time.sleep(0.5)
