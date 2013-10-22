import pygame
import threading
import sys
from pygame.locals import *
from lib.statemachine import StateMachine
from config import Config as cfg
from lib.sprite import Sprite

class Scene(StateMachine):

    def __init__(self):
        super().__init__()
        #self.input_thread = threading.Thread(None, self.input)
        #self.prep_thread = threading.Thread(None, self.process)
        #self.render_thread = threading.Thread(None, self.render)
        self.event = None
        self.buffer = pygame.Surface((cfg.SCENE_WIDTH, cfg.SCENE_HEIGHT))
        
    def update(self):
        if(self.state == 0):
            self.load()
            #self.input_thread.start()
            #self.prep_thread.start()
            #self.render_thread.start()
            self.state = 1
        if(self.state == 1):
            self.input()
            self.process()
            self.render()
            
    def load(self):
        pass
            
    def input(self):
        pass
    
    def process(self):
        pass
    
    def render(self):
        pass
        