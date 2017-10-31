import pygame

WIDTH=100
HEIGHT=100

class ScoreLayer(pygame.sprite.Sprite):
    def __init__(self, surface, font):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.score = 0
        self.generation = 0
        self.mutated = 0
        self.font = font
        self.update_image()

    def update_image(self):
        scoreImage = self.font.render('SCORE: {}'.format(self.score), True, (30,30,30))
        genImage = self.font.render('GEN: {}'.format(self.generation), True, (30,30,30))
        mutatedImage = self.font.render('MUT: {}'.format(self.mutated), True, (30,30,30))
        r = [scoreImage.get_rect(), genImage.get_rect(), mutatedImage.get_rect()]
        self.image = pygame.Surface([max([x.width for x in r]), sum([x.height for x in r]) + len(r) * 5], pygame.SRCALPHA, 32).convert_alpha()
        self.image.blit(scoreImage, (0, 0))
        self.image.blit(genImage, (0, r[0].height + 5))
        self.image.blit(mutatedImage, (0, r[0].height + r[1].height + 10))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def get_line(self):
        return '\n'.join(['SCORE: {}'.format(self.score), 'GEN: {}'.format(self.generation)])

    def set_score(self, score):
        self.score = score
        self.update_image()

    def set_generation(self, generation):
        self.generation = generation
        self.update_image()

    def set_mutation(self, mutation):
        self.mutated = mutation
        self.update_image()
