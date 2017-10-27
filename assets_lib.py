import pygame

basket = None
egg = None
stone = None

def init():
    global basket, egg, stone
    basket = pygame.image.load('./assets/basket.png').convert_alpha()
    rect = basket.get_rect()
    basket = pygame.transform.scale(basket, (rect.width/2, rect.height/2))
    egg = pygame.image.load('./assets/egg.png').convert_alpha()
    rect = egg.get_rect()
    egg = pygame.transform.scale(egg, (rect.width/4, rect.height/4))
    stone = pygame.image.load('./assets/stone-small.png').convert_alpha()
    rect = stone.get_rect()
    stone = pygame.transform.scale(stone, (rect.width/2, rect.height/2))
