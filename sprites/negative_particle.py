import pygame

WIDTH=10
HEIGHT=10
SCALE = 25
PATH='./assets/stone.png'

class NegativeParticle(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PATH).convert_alpha()
        rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (rect.width/SCALE, rect.height/SCALE))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.velocity = velocity

    def update(self):
        point = self.rect.center
        self.rect.center = (point[0] + self.velocity[0], point[1]+self.velocity[1])
        width, height = pygame.display.get_surface().get_size()
        if not( -100 < self.rect.topleft[1] <= height + 10):
           self.kill()
