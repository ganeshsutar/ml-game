import pygame
import random
from sklearn.neural_network import MLPClassifier
from game_scene import GameScene
from genetic_algo import GeneticAlgo


PARTICLE_RATE = 1000

class MainScene:
    def __init__(self, no_of_games, screen_width, screen_height):
        self.no_of_games = no_of_games
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_scene_height = screen_height
        self.game_scene_width = screen_width / self.no_of_games
        self.genetic_algo = GeneticAlgo(self.no_of_games, self)
        self.reinit()

    def reinit(self):
        self.last_added = pygame.time.get_ticks()
        self.scenes = []
        for i in range(self.no_of_games):
            game_scene = GameScene((self.game_scene_width, self.game_scene_height))
            self.scenes.append(game_scene)

    def update(self, timeDelta):
        self.take_move()
        running = False
        for scene in self.scenes:
            scene.update(timeDelta)
            running = (not scene.game_over) or running
        self.add_particle()
        if not running:
            self.genetic_algo.add_generation()
            self.reinit()

    def draw(self, timeDelta):
        screen = pygame.display.get_surface()
        for i, scene in enumerate(self.scenes):
            scene.draw(timeDelta)
            pos = (i*self.game_scene_width, 0)
            screen.blit(scene.surface, pos)
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(pos, (self.game_scene_width, self.game_scene_height)), 1)

    def add_particle(self):
        current_time = pygame.time.get_ticks()
        if( current_time - self.last_added < PARTICLE_RATE ):
            return
        vy = random.randint(3, 8)
        pos = (random.randint(0,self.game_scene_width), -50)
        positivity = random.randint(0, 1)
        for scene in self.scenes:
            scene.add_particle(pos, vy, positivity)
        self.last_added = current_time

    def init_nn(self):
        self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
        X = [[0 for x in range(32)] for i in range(3)]
        y = [-1, 0, 1]
        self.clf.fit(X, y)

    def take_move(self):
        for i, scene in enumerate(self.scenes):
            if not scene.game_over:
                x = scene.get_inputs(3)
                y = self.genetic_algo.predict(i, x)
                if y == -1:
                    scene.move_slider(pygame.K_LEFT)
                elif y == 1:
                    scene.move_slider(pygame.K_RIGHT)
