import pygame
from lib.animation import Animation

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, width, height, file):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height       
        self.animation = Animation([])
        self.file = file
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect() 
    
    def update(self):
        self.animation.update()
        self.surface.blit(self.animation.get_frame(), self.rect)
        
    def load(self, fps = 30):
        image = pygame.image.load(self.file)
        image.convert()
        
        #TODO: avoid decimals
        rows = int(image.get_height() / self.height)
        cols = int(image.get_width() / self.width)
        
        frames = []
        
        for r in range(rows):
            for c in range(cols):
                frame = pygame.Surface((self.width, self.height))
                frame.blit(image, (c*self.width, -r*self.height))
                frames.append(frame)
                
        self.animation = Animation(frames, fps)