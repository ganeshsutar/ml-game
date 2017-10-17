import pygame

WIDTH=10
HEIGHT=10
PATH='./assets/egg.png'

class PositiveParticle(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PATH).convert_alpha()
        rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (rect.width/2, rect.height/2))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.velocity = velocity
        

    def update(self):
        point = self.rect.center
        self.rect.center = (point[0] + self.velocity[0], point[1]+self.velocity[1])
        width, height = pygame.display.get_surface().get_size()
        if not (-100 < self.rect.topleft[1] <= height + 10):
            self.kill()
