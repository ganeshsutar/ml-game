import pygame
import random

from sprites import Slider, PositiveParticle, NegativeParticle
from layers import ScoreLayer

PARTICLE_RATE = 500

class GameScene:
    def __init__(self, (game_width, game_height)):
        print(game_width, game_height)
        self.surface = pygame.Surface((game_width, game_height), pygame.SRCALPHA, 32).convert_alpha()
        self.slider = Slider(self.surface)
        self.sliderSprites  = pygame.sprite.RenderPlain()
        self.positiveParticles = pygame.sprite.RenderPlain()
        self.negativeParticles = pygame.sprite.RenderPlain()
        self.layers = pygame.sprite.RenderPlain()

        self.sliderSprites.add(self.slider)

        self.game_over = False
        self.game_last_drawn = False

        self.score_layer = ScoreLayer(self.surface)
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

    def move_slider(self, label):
        self.slider.move(label)

    def draw(self, timeDelta):
        if self.game_last_drawn == True:
            return
        self.surface.fill((255,255,255))
        self.sliderSprites.draw(self.surface)
        self.positiveParticles.draw(self.surface)
        self.negativeParticles.draw(self.surface)
        self.layers.draw(self.surface)
        if self.game_over == True:
            self.game_last_drawn = True

    def add_particle(self, pos, vy, positivity):
        if self.game_over:
            return
        if positivity == 0:
            self.positiveParticles.add( PositiveParticle(self.surface, pos, (0, vy)) )
        else:
            self.negativeParticles.add( NegativeParticle(self.surface, pos, (0, vy)) )
