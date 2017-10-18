import pygame
import random
from game_scene import GameScene

PARTICLE_RATE = 1000

class CaptureInputScene:
    def __init__(self):
        self.width, self.height = pygame.display.get_surface().get_size()
        self.game_scene_width = 400
        self.game_scene_height = 300
        self.scene = GameScene((self.game_scene_width, self.game_scene_height))
        self.last_added = pygame.time.get_ticks()
        self.X = []
        self.y = []


    def update(self, timeDelta):
        self.add_particle()
        keys = pygame.key.get_pressed()
        move = 0
        if keys[pygame.K_LEFT] != 0:
            self.scene.move_slider(pygame.K_LEFT)
            move = -1
        elif keys[pygame.K_RIGHT]:
            self.scene.move_slider(pygame.K_RIGHT)
            move = 1
        self.scene.update(timeDelta)
        self.X.append(self.scene.get_inputs(3))
        self.y.append(move)


    def draw(self, timeDelta):
        self.scene.draw(timeDelta)
        screen = pygame.display.get_surface()
        scaled = pygame.transform.scale(self.scene.surface, (self.width, self.height))
        screen.blit(scaled, (0,0))


    def add_particle(self):
        current_time = pygame.time.get_ticks()
        if( current_time - self.last_added < PARTICLE_RATE ):
            return
        vy = random.randint(3, 8)
        pos = (random.randint(0,self.game_scene_width), -50)
        positivity = random.randint(0, 1)
        self.scene.add_particle(pos, vy, positivity)
        self.last_added = current_time
