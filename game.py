import time
import numpy as np
import pygame
from pygame.locals import *

from grid import Grid

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 400, 400

        self.grid = Grid(20, 20)

        if self.grid.setGrid(np.random.randint(0, 2, (20, 20))):
            print("successfully set grid")

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        self.grid.update()

    def on_render(self):
        self.grid.draw(self._display_surf, self.width, self.height)

    def on_cleanup(self):
        pygame.quit()

    def on_excute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            time.sleep(1)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.on_loop()
        self.on_cleanup()
