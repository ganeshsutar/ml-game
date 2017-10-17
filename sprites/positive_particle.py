import pygame

WIDTH=10
HEIGHT=10
PATH='./assets/egg.png'

class PositiveParticle(pygame.sprite.Sprite):
    def __init__(self, surface, position, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.image = pygame.image.load(PATH).convert_alpha()
        rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (rect.width/2, rect.height/2))
        self.rect = self.image.get_rect()
        # pygame.draw.rect(self.image,(0, 255, 0),(0, 0, self.rect.width-1,self.rect.height -1),1)
        self.rect.center = position
        self.velocity = velocity


    def update(self):
        point = self.rect.center
        self.rect.center = (point[0] + self.velocity[0], point[1]+self.velocity[1])
        width, height = self.surface.get_size()
        if not (-100 < self.rect.topleft[1] <= height + 10):
            self.kill()

    def get_inputs(self):
        return (1, self.rect.center.x, self.rect.center.y, self.velocity[1])
