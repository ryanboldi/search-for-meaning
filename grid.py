import unittest

import numpy
import pygame

from utils import getColor

class Grid:
    def __init__(self, width, height, colors = 3):
        "width, height measured in # of cells"
        self._width = width
        self._height = height
        self._colors = colors
        self._grid = numpy.zeros((self._width, self._height, self._colors))

    def getWdith(self):
        return self._width
    
    def getHeight(self):
        return self._height

    def getInGrid(self, x, y):
        if (x >= self._width):
            return None
        elif (y >= self._height):
            return None
        else:
            return self._grid[x][y]

    def setInGrid(self, x, y, val):
        if (x >= self._width):
            return False
        elif (y >= self._height):
            return False
        else:
            self._grid[x][y] = val
            return True
    
    def draw(self, surface, draw_width, draw_height):
        cell_width = draw_width / self._width
        cell_height = draw_height / self._height

        line_thickness = 0

        surface.fill((255, 255, 255))

        for x in range(0, self._width):
            for y in range(0, self._height):
                pygame.draw.rect(surface, getColor(self.getInGrid(x, y)), pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height))

        for vert_line in range (0, self._width + 1):
            pygame.draw.line(surface, (0, 0, 0), (vert_line * cell_width, 0), (vert_line * cell_width, draw_height), width=line_thickness)

        for horiz_line in range (0, self._height + 1):
            pygame.draw.line(surface, (0, 0, 0), (0, horiz_line * cell_height), (draw_width, horiz_line * cell_height), width=line_thickness)


        pygame.display.update()


# UNIT TESTING
class TestGridClass(unittest.TestCase):
    def testSizeCorrect(self):
        grid = Grid(3, 4)
        self.assertEqual(grid.getInGrid(2, 0)[0], 0)
        self.assertEqual(grid.getInGrid(2, 3)[0], 0)
    
    def testSetInGrid(self):
        grid = Grid(3, 4)
        self.assertFalse(grid.setInGrid(5, 5, [50, 50, 50]))
        self.assertTrue(grid.setInGrid(2, 3, [100, 100, 100]))
        self.assertEqual(grid.getInGrid(2, 3)[0], 100)
        self.assertEqual(grid.getInGrid(2, 3)[1], 100)
        self.assertEqual(grid.getInGrid(2, 3)[2], 100)

unittest.main()