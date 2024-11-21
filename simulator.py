import random
import math
from matplotlib import pyplot as plt
import numpy as np
import csv


def image_example():
    '''should produce red,purple,green squares
    on the diagonal, over a black background'''
    # RGB indexes
    red, green, blue = range(3)
    # img array
    # all zeros = black pixels
    # shape: (150 rows, 150 cols, 3 colors)
    img = np.zeros((150, 150, 3))
    for x in range(50):
        for y in range(50):
            # red pixels
            img[x, y, red] = 1.0
            # purple pixels
            # set 3 color components
            img[x + 50, y + 50, :] = (.5, .0, .5)
            # green pixels
            img[x + 100, y + 100, green] = 1.0
    plt.imshow(img)


def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly.
    """
    var = float(sd)**2
    denom = (2 * math.pi * var)**.5
    num = math.exp(-(float(x) - float(mean))**2 / (2 * var))
    return num / denom


def pdeath(x, mean, sd):
    start = x - 0.5
    end = x + 0.5
    step = 0.01
    integral = 0.0
    while start <= end:
        integral += step * (normpdf(start, mean, sd) +
                            normpdf(start + step, mean, sd)) / 2
        start += step
    return integral


recovery_time = 4  # recovery time in time-steps
virality = 0.2  # probability that a neighbor cell is infected in
# each time step


class Cell(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "S"  # can be "S" (susceptible), "R" (resistant = dead), or
        # "I" (infected)
        self.time = 0

    def infect(self):  # Step 2.1
        pass

    def process(self, adjacent_cells):  # Step 2.3
        pass


class Map(object):

    def __init__(self):
        self.height = 150
        self.width = 150
        self.cells = {}

    def add_cell(self, cell):  # Step 1.1
        self.cells[(cell.x, cell.y)] = cell

    def display(self):  # Step 1.3
        image = np.zeros((self.height, self.width, 3))
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.cells.keys():
                    state = self.cells[(x, y)].state
                    if state == 's':
                        image[x, y] = (0, 255, 0)
                    elif state == 'r':
                        image[x, y] = (128, 128, 128)
                    elif state == 'i':
                        image[x, y] = (255, 0, 0)
                else:
                    image[x, y] = (0, 0, 0)

        plt.imshow(image)  # display the map

    def adjacent_cells(self, x, y):  # Step 2.2
        pass


def read_map(filename):

    m = Map()
    file = open("nyc_map.csv", 'r')  #open the file
    data_reader = csv.reader(file)
    for cell in data_reader:
        m.add_cell(Cell(cell[0], cell[1]))
    # ... Write this function, Step 1.2

    return m


m = read_map("nyc_map.csv")
m.display()
