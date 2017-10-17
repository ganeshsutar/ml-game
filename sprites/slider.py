import pygame
from vector import Vec2d as vec

BASKET_ACC = 3
BASKET_FRICTION = 0.12
WIDTH=30
HEIGHT= 10
PATH = './assets/basket.png'

class Slider(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.image = pygame.image.load(PATH).convert_alpha()
        rect = self.image.get_rect()
        # pygame.draw.rect(self.image,(0, 0, 255),(0, 0, rect.width-1,rect.height -1),1)
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        width,height = self.surface.get_size()
        self.rect.center = (width/2,height-HEIGHT-10);
        self.pos = vec(width/2,height-HEIGHT-10)
        # self.velocity = velocity

    def move(self, label):
        self.acc = vec(0,0)
        if label == pygame.K_LEFT:
           self.acc.x = -BASKET_ACC
        if label ==pygame.K_RIGHT:
           self.acc.x = BASKET_ACC

        self.acc += self.vel * (-BASKET_FRICTION)
        self.vel += self.acc
        self.pos += (self.vel + 0.5 * self.acc)
        # print(self.acc, self.vel, self.pos)

        screenSize = self.surface.get_size()
        if self.pos.x < 0: self.pos.x = 0
        if self.pos.x > screenSize[0]: self.pos.x = screenSize[0]
        if self.pos.y < 0: self.pos.y = 0
        if self.pos.y > screenSize[1]: self.pos.y = screenSize[1]

        self.rect.center = self.pos

    def get_inputs(self):
        return (self.rect.center[0])
