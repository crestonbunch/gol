import pygame
import os
from lib.character import Character
from lib.sprite import Sprite
from lib.animation import Animation
from config import Config as cfg

class Organism(Character):

    def __init__(self):
        super().__init__()
        self.sprites = {
            'grow':Sprite(cfg.ORG_WIDTH, cfg.ORG_HEIGHT, os.path.join(cfg.IMG_DIR, cfg.SPRITE_GROW)),
            'live':Sprite(cfg.ORG_WIDTH, cfg.ORG_HEIGHT, os.path.join(cfg.IMG_DIR, cfg.SPRITE_LIVE))
        }
        self.sprite = self.sprites['grow']
    
    def update(self):
        if self.state == 0:
            # begin the grow animation
            self.sprite = self.sprites['grow']
            self.sprite.load()
            self.state = 1
        elif self.state == 1:
            # move on when the animation is complete
            if(self.sprite.animation.cycles > 0):
                self.state = 2
        elif self.state == 2:
            # begin the living animation
            self.sprite = self.sprites['live']
            self.sprite.load()
            self.state = 3
        elif self.state == 3:
            pass
        
        self.sprite.update()