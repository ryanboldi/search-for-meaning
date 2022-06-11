import pygame
from pygame.locals import *
from grid import Grid

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 600, 600

        self.grid = Grid(50, 50)
        #self.grid.setInGrid(5, 5, 1)

        for i in range(0, 50):
            for j in range(0, 50):
                self.grid.setInGrid(i, j, i/100 + j/100)
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        pass    

    def on_render(self):
        self.grid.draw(self._display_surf, self.width, self.height)

    def on_cleanup(self):
        pygame.quit()

    def on_excute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
