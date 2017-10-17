#! /usr/bin/python

import pygame
import os
import random
from main_scene import MainScene

def main():
    pygame.init()
    screen = pygame.display.set_mode((1300,600))
    pygame.display.set_caption('EGG CATCHER')
    pygame.font.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()
    keepGoing  = True
    width, height = screen.get_size()
    main_scene = MainScene(4, width, height)

    while keepGoing:
        timeDelta = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        main_scene.update(timeDelta)
        main_scene.draw(timeDelta)
        #pygame.draw.rect(screen,(0,128,255), pygame.Rect(30,30,60,60))
        pygame.display.flip()

if __name__ == "__main__":
    main()
