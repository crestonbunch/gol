import pygame, math
from lib.character import Character
from lib.camera import Camera
from objects.organism import Organism
from config import Config as cfg

class Grid(Character):

    def __init__(self):
        super().__init__()
        self.organisms = {}
        self.camera = Camera(cfg.SCENE_WIDTH, cfg.SCENE_HEIGHT)
        self.surface = pygame.Surface((cfg.SCENE_WIDTH, cfg.SCENE_HEIGHT))
        self.zoom = 1
        self.play = False
        self.clock = pygame.time.Clock()
        self.interval = 0
    
    def update(self, event):
        
        zw = int(cfg.ORG_WIDTH*self.zoom)
        zh = int(cfg.ORG_HEIGHT*self.zoom)
            
        if event.type == pygame.MOUSEMOTION:
            # Mouse position
            pos = event.pos
            # Mouse velocity
            vel = event.rel
            
            # Add organisms when drawing
            if event.buttons == (True, False, False):
                x = int((pos[0]/ zw + self.camera.x) )
                y = int((pos[1]/ zh + self.camera.y) )
                self.organisms[(x, y)] = Organism()
            # Move the viewport
            if event.buttons == (False, True, False):
                dx = -int(vel[0]) / zw
                dy = -int(vel[1]) / zh
                self.camera.move(dx, dy)
            # delete organisms
            if event.buttons == (False, False, True):
                x = int((pos[0]/ zw + self.camera.x) )
                y = int((pos[1]/ zh + self.camera.y) )
                if (x, y) in self.organisms.keys():
                    del(self.organisms[(x, y)])
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 5:
                # zoom smaller
                self.zoom = self.zoom * .9
            if event.button == 4:
                # zoom larger
                self.zoom = self.zoom * 1.1
        
        if event.type == pygame.KEYUP:
            self.play = not self.play
        
        if self.play:
            self.interval = self.interval + self.clock.tick()
            if self.interval > 1000 / cfg.GRID_FPS:
                self.interval = 0
                self.generate()
        
        # Blit organisms that are in view
        self.surface.fill((255,255,255))
        visible = self.camera.focus(self.organisms, self.zoom)
        for (x, y) in visible:
            org = visible[(x, y)]
            #TODO: call these functions only once when necessary, not every iteration
            if not self.play:
                org.sprite.animation.pause()
            else:
                org.sprite.animation.unpause()
            org.update()
            # scale the sprite surface to the zoom factor
            zoomed = pygame.transform.scale(org.sprite.surface, (zw, zh))
            self.surface.blit(zoomed, (
            (x - self.camera.x) * zw,
            (y - self.camera.y) * zh
            ))
            
    def generate(self):
        new = {}
        for coord in self.organisms.keys():
            org = self.organisms[coord]
            neighbors = self.live_neighbors(coord)
            
            # determine if the organism should remain alive
            if neighbors <= 1:
                pass
            elif neighbors >= 4:
                pass
            else:
                new[coord] = org
                
            # get a list of nearby dead organisms
            dead = self.dead_neighbors(coord)
            for coord in dead:
                # resurrect it if it has 3 living neighbors
                neighbors = self.live_neighbors(coord)
                if neighbors == 3:
                    new[coord] = Organism()
                    
        self.organisms = new
    
    def dead_neighbors(self, pos):
        coords = []
        for i in range(-1,2):
            for z in range(-1,2):
                rpos = (pos[0]+i,pos[1]+z)
                if not rpos in self.organisms.keys():
                    coords.append(rpos)
        return coords
        
    def live_neighbors(self, pos):
        n = 0
        for i in range(-1,2):
            for z in range(-1,2):
                rpos = (pos[0]+i,pos[1]+z)
                if rpos in self.organisms.keys() and not rpos == pos:
                    n = n + 1
        return n
            