import pygame
import random
from sprites import Slider, PositiveParticle, NegativeParticle
from layers import ScoreLayer

PARTICLE_RATE = 500

class GameScene:
    def __init__(self):
        self.slider = Slider((100, 100))
        self.sliderSprites  = pygame.sprite.RenderPlain()
        self.sliderSprites.add(self.slider)

        self.positiveParticles = pygame.sprite.RenderPlain()
        self.negativeParticles = pygame.sprite.RenderPlain()
        self.lastParticleAdded = pygame.time.get_ticks()

        self.layers = pygame.sprite.RenderPlain()
        self.score_layer = ScoreLayer()
        self.layers.add(self.score_layer)

    def update(self, timeDelta):
        self.sliderSprites.update()
        self.positiveParticles.update()
        self.negativeParticles.update()

    def draw(self, timeDelta):
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
