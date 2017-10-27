#! /usr/bin/python

import pygame
import os
import random
import pandas as pd
import assets_lib
from main_scene import MainScene
from capture_input import CaptureInputScene

def save_output(main_scene):
    if type(main_scene) == type(CaptureInputScene()):
        print('Saving files')
        X = pd.DataFrame(main_scene.X, columns = [chr(ord('A')+i) for i in range(len(main_scene.X[0]))])
        y = pd.DataFrame(main_scene.y, columns = ['move'])
        X.to_csv('./input.csv', index=False)
        y.to_csv('./output.csv', index=False)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1024,768))
    pygame.display.set_caption('EGG CATCHER')
    pygame.font.init()
    pygame.mixer.init()

    assets_lib.init()
    clock = pygame.time.Clock()
    keepGoing  = True
    width, height = screen.get_size()
    main_scene = MainScene(4, 5)
    # main_scene = CaptureInputScene()

    while keepGoing:
        timeDelta = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q] != 0:
                    keepGoing = False

        main_scene.update(timeDelta)
        main_scene.draw(timeDelta)
        #pygame.draw.rect(screen,(0,128,255), pygame.Rect(30,30,60,60))
        pygame.display.flip()
    # save_output(main_scene)

if __name__ == "__main__":
    main()
