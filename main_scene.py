import pygame
import random
from sklearn.neural_network import MLPClassifier
from game_scene import GameScene


PARTICLE_RATE = 1000

class MainScene:
    def __init__(self, no_of_games, screen_width, screen_height):
        self.no_of_games = no_of_games
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_scene_height = screen_height
        self.game_scene_width = screen_width / self.no_of_games
        self.last_added = pygame.time.get_ticks()

        self.scenes = []
        for i in range(self.no_of_games):
            game_scene = GameScene((self.game_scene_width, self.game_scene_height))
            self.scenes.append(game_scene)

        self.init_nn()

    def update(self, timeDelta):
        self.take_move()
        for scene in self.scenes:
            scene.update(timeDelta)
        self.add_particle()

    def draw(self, timeDelta):
        screen = pygame.display.get_surface()
        for i, scene in enumerate(self.scenes):
            scene.draw(timeDelta)
            pos = (i*self.game_scene_width, 0)
            screen.blit(scene.surface, pos)

    def add_particle(self):
        current_time = pygame.time.get_ticks()
        if( current_time - self.last_added < PARTICLE_RATE ):
            return
        vy = random.randint(3, 8)
        pos = (random.randint(0,self.game_scene_width-100), -50)
        positivity = random.randint(0, 1)
        for scene in self.scenes:
            scene.add_particle(pos, vy, positivity)
        self.last_added = current_time

    def init_nn(self):
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
        X = [[0 for x in range(32)] for i in range(3)]
        y = [-1, 0, 1]
        print(X, y)
        self.clf.fit(X, y)

    def take_move(self):
        X = [scene.get_inputs(3) for scene in self.scenes]
        print(X)
        y = self.clf.predict(X)
        for i in range(len(y)):
            move = y[i]
            scene = self.scenes[i]
            if move == -1:
                scene.move_slider(pygame.K_LEFT)
            elif move == 1:
                scene.move_slider(pygame.K_RIGHT)
