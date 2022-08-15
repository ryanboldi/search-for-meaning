import unittest

import math
import numpy as np
import pygame

import torch.nn.functional as F
import torch

from utils import getColor, conv3D2, sigmoid

class Grid:
    def __init__(self, width, height):
        "width, height measured in # of cells"
        self._width = width
        self._height = height
        self._grid = np.zeros((self._width, self._height))

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

    def setGrid(self, val):
        #first two dims have to be the same (w, h)
        if (val.shape[:2] == self._grid.shape[:2]):
            self._grid = val
            return True
        return False

    def draw(self, surface, draw_width, draw_height):
        print(self._grid[0])
        cell_width = draw_width / self._width
        cell_height = draw_height / self._height

        line_thickness = 1

        surface.fill((255, 255, 255))

        for x in range(0, self._width):
            for y in range(0, self._height):
                pygame.draw.rect(surface, getColor(self.getInGrid(x, y)), pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height))

        for vert_line in range (0, self._width + 1):
            pygame.draw.line(surface, (0,0,0), (vert_line * cell_width, 0), (vert_line * cell_width, draw_height), width=line_thickness)

        for horiz_line in range (0, self._height + 1):
            pygame.draw.line(surface, (0,0,0), (0, horiz_line * cell_height), (draw_width, horiz_line * cell_height), width=line_thickness)

        pygame.display.update()

    def update(self):
        temp = torch.reshape(torch.from_numpy(self._grid), (1, 1, self._height, self._width)).double()
        print(temp.shape)

        weights = torch.from_numpy(np.array([[1, 0, 1],[0, 0, 1], [0, 1, 0]])).double()
        weights = torch.reshape(weights, (1, 1, 3, 3))

        new_grid = F.conv2d(temp, weights, padding=1)
        new_grid = torch.reshape(new_grid, (20, 20))
        new_grid = new_grid/6
        self._grid = sigmoid(new_grid.numpy()[:, :])

        #must use a 3x3x3 arr as conv kernal
        #do nothing
        #self._grid = sigmoid(conv3D2(self._grid, np.array([[[1, 1, 1],[1, 1, 1], [0, 0, 0]],
         #                                                   [[1, 1, 1],[1, 1, 1], [0, 0, 0]],
          #                                                  [[1, 1, 1],[1, 1, 1], [0, 0, 0]]]), 1))
        pass

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

#unittest.main()