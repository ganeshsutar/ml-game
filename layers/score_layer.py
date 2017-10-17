import pygame

WIDTH=100
HEIGHT=100

class ScoreLayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.font = pygame.font.SysFont('Ubuntu Mono', 15)
        self.update_score()

    def update_score(self):
        width, height = pygame.display.get_surface().get_size()
        self.image = self.font.render('SCORE: {}'.format(self.score), True, (30,30,30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (width-self.rect.width-20, 20)
