import pygame

class Slider(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 30],pygame.SRCALPHA,32).convert_alpha()
        pygame.draw.rect(self.image,(0, 0, 255),(0, 0, 30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = position
        # self.velocity = velocity

    def update(self):
        point = self.rect.center
        self.rect.center = (point[0],point[1]+1)
