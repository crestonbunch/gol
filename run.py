import pygame
from pygame.locals import *
from config import Config as cfg
from lib.scene import Scene
from scenes.play import PlayScene

class App:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT))
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        
        self.play = True
        
        self.scene = PlayScene()
        
        while self.play:
            self.tick();
            self.scene.update()
            self.window.blit(self.scene.buffer, (0,0))
            pygame.display.update()
        
    def tick(self):
        self.clock.tick(cfg.FRAMES_PER_SEC)
     
        
game = App()
