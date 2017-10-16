#! /usr/bin/python

import pygame
import os
from game_scene import GameScene



def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('EGG CATCHER')
    pygame.font.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()
    scene = GameScene()
    keepGoing  = True
    while keepGoing:
        timeDelta = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        scene.update(timeDelta)
        scene.draw(timeDelta)
        #pygame.draw.rect(screen,(0,128,255), pygame.Rect(30,30,60,60))
        pygame.display.flip()
if __name__ == "__main__":
    main()
