#! /usr/bin/python

import pygame
import os
import random
from game_scene import GameScene


PARTICLE_RATE = 1000

def get_particle(last_added, width, height):
    current_time = pygame.time.get_ticks()
    if( current_time - last_added < PARTICLE_RATE ):
        return False
    vy = random.randint(3, 8)
    pos = (random.randint(0,width-100), -50)
    positivity = random.randint(0, 1)
    return (pos, vy, positivity)



def main():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('EGG CATCHER')
    pygame.font.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()
    surfaces = [pygame.Surface((300, 600), pygame.SRCALPHA, 32).convert_alpha(),
        pygame.Surface((300, 600), pygame.SRCALPHA, 32).convert_alpha()]
    scenes = [GameScene(surfaces[0]), GameScene(surfaces[1])]
    keepGoing  = True
    current_time = pygame.time.get_ticks()
    while keepGoing:
        timeDelta = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        particle = get_particle(current_time, 300, 600)
        if particle:
            for scene in scenes:
                scene.add_particle(*particle)
            current_time = pygame.time.get_ticks()
        for scene in scenes:
            scene.update(timeDelta)
            scene.draw(timeDelta)
        #pygame.draw.rect(screen,(0,128,255), pygame.Rect(30,30,60,60))
        for i, surface in enumerate(surfaces):
            rect = surface.get_rect()
            rect.topleft = (i*300, 0)
            screen.blit(surface, rect)
        pygame.display.flip()
if __name__ == "__main__":
    main()
