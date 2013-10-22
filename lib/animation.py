import pygame

class Animation:
    
    def __init__(self, frames, fps = 30):
        self.frames = frames
        self.position = 0;
        self.clock = pygame.time.Clock()
        self.interval = 0
        self.fps = fps
        self.cycles = 0
        self.paused = False
    
    def next(self):
        self.position = self.position + 1
        if self.position >= len(self.frames):
            self.position = 0
            # count the number of times the animation has completed
            self.cycles = self.cycles + 1
    '''
    def prev(self):
        self.position = self.position - 1
        if self.position < 0:
            self.position = len(self.frames) - 1
    '''
    def get_frame(self):
        return self.frames[self.position]
        
    def update(self):
        # advance the frame when the interval meets the FPS
        self.interval = self.interval + self.clock.tick()
        if self.interval > 1000 / self.fps:
            if not self.paused:
                self.next()
            self.interval = 0
            
    def pause(self):
        self.paused = True
    
    def unpause(self):
        self.paused = False
        