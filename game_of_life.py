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
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.cells = [[Cell(random.choice((False, True))) for i in range(column)] for i in range(row)]

    def show(self):
        for row in self.cells:
            for cell in row:
                print(cell, end='')
            print()

    def calculate_neighbour(self):
        cells = self.cells
        row = self.row
        column = self.column
        for y in range(row):
            for x in range(column):
                if cells[y - 1][x - 1].state:
                    cells[y][x].neighbour += 1
                if cells[y - 1][x].state:
                    cells[y][x].neighbour += 1
                if cells[y - 1][(x + 1) % column].state:
                    cells[y][x].neighbour += 1
                if cells[y][x - 1].state:
                    cells[y][x].neighbour += 1
                if cells[y][(x + 1) % column].state:
                    cells[y][x].neighbour += 1
                if cells[(y + 1) % row][x - 1].state:
                    cells[y][x].neighbour += 1
                if cells[(y + 1) % row][x].state:
                    cells[y][x].neighbour += 1
                if cells[(y + 1) % row][(x + 1) % column].state:
                    cells[y][x].neighbour += 1

    def calculate_next_state(self):
        cells = self.cells
        for y in range(self.row):
            for x in range(self.column):
                if cells[y][x].state:
                    if cells[y][x].neighbour in (2, 3):
                        cells[y][x].state = True
                    else:
                        cells[y][x].state = False
                else:
                    if cells[y][x].neighbour == 3:
                        cells[y][x].state = True
                cells[y][x].neighbour = 0

    def evolve(self):
        self.calculate_neighbour()
        self.calculate_next_state()

if __name__ == '__main__':
    u = Universe(24, 40)
    for i in range(3600):
        os.system('clear')
        u.show()
        u.evolve()
        time.sleep(0.5)
