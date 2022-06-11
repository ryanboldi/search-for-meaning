import unittest
import pygame
import numpy

class Grid:
    def __init__(self, width, height):
        "width, height measured in # of cells"
        self._width = width
        self._height = height
        self._grid = numpy.zeros((self._width, self._height))

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

        surface.fill((255, 255, 255))
        pygame.draw.circle(surface, (255, 35, 70), (100,100), 50)
        pygame.display.update()


# UNIT TESTING
class TestGridClass(unittest.TestCase):
    def testSizeCorrect(self):
        grid = Grid(3, 4)
        self.assertEqual(grid.getInGrid(2, 0), 0)
        self.assertEqual(grid.getInGrid(2, 3), 0)
    
    def testSetInGrid(self):
        grid = Grid(3, 4)
        self.assertFalse(grid.setInGrid(5, 5, 50))
        self.assertTrue(grid.setInGrid(2, 3, 100))
        self.assertEqual(grid.getInGrid(2, 3), 100)

#unittest.main()