import unittest
import numpy

class Grid:
    def __init__(self, width, height):
        "width, height measured in # of boxes"
        self.width = width
        self.height = height
        self.grid = numpy.zeros((self.width, self.height))
        print(self.grid)

