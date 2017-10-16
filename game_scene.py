import pygame
from sprites import Slider

class GameScene:
    def __init__(self):
        self.slider = Slider((100, 100))
        self.sliderSprites  = pygame.sprite.RenderPlain()
        self.sliderSprites.add(self.slider)

    def update(self, timeDelta):
        self.sliderSprites.update()

    def draw(self, timeDelta):
        screen = pygame.display.get_surface()
        screen.fill((255,255,255))
        self.sliderSprites.draw(screen)
