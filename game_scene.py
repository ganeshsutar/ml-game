import pygame
import random

from sprites import Slider, PositiveParticle, NegativeParticle
from layers import ScoreLayer

PARTICLE_RATE = 500

class GameScene:
    def __init__(self):
        self.slider = Slider()
        self.sliderSprites  = pygame.sprite.RenderPlain()
        self.sliderSprites.add(self.slider)
        self.game_over = False
        self.game_last_drawn = False
        self.positiveParticles = pygame.sprite.RenderPlain()
        self.negativeParticles = pygame.sprite.RenderPlain()
        self.lastParticleAdded = pygame.time.get_ticks()

        self.layers = pygame.sprite.RenderPlain()
        self.score_layer = ScoreLayer()
        self.layers.add(self.score_layer)


    def update(self, timeDelta):
        if self.game_over == True:
            return
        self.sliderSprites.update()
        self.positiveParticles.update()
        self.negativeParticles.update()
        collide_dict = pygame.sprite.groupcollide(self.sliderSprites,self.positiveParticles,False,True)
        for x in collide_dict:
            self.score_layer.set_score(self.score_layer.score+10)
        collide_dict = pygame.sprite.groupcollide(self.sliderSprites,self.negativeParticles,False,False)
        if len(collide_dict)>0:
            self.game_over = True

    def draw(self, timeDelta):
        if self.game_last_drawn == True:
            return
        screen = pygame.display.get_surface()
        screen.fill((255,255,255))
        current_time = pygame.time.get_ticks()
        if (current_time - self.lastParticleAdded) > PARTICLE_RATE:
            self.add_particle()
            self.lastParticleAdded = current_time
        self.sliderSprites.draw(screen)
        self.positiveParticles.draw(screen)
        self.negativeParticles.draw(screen)
        self.layers.draw(screen)
        if self.game_over == True:
            self.game_last_drawn = True

    def add_particle(self):
        # randomly add a particle
        width, height = pygame.display.get_surface().get_size()
        vy = random.randint(3, 8)
        pos = (random.randint(0,width-100), -50)
        positivity = random.randint(0, 1)
        if positivity == 0:
            self.positiveParticles.add( PositiveParticle(pos, (0, vy)) )
        else:
            self.negativeParticles.add( NegativeParticle(pos, (0, vy)) )
