import pygame, sys
from lib.scene import Scene
from objects.grid import Grid

class PlayScene(Scene):
    
    def __init__(self):
        super().__init__()
    
    def load(self):
        self.grid = Grid()
            
    def input(self):
        self.event = pygame.event.poll()
    
    def process(self):
        self.grid.update(self.event)
        if self.event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    def render(self):
        #self.buffer.fill((0,0,0))
        self.buffer.blit(self.grid.surface, (0,0))