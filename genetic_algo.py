from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import random
import pandas as pd

base_X = None
base_Y = None
scaler = None

try:
    base_X = pd.read_csv('./input-Y.csv')
    base_y = pd.read_csv('./output-Y.csv')
    scaler = StandardScaler()
    scaler.fit(base_X)
    base_X = scaler.transform(base_X)
except:
    pass

def make_nn():
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 3), random_state=None)
    if not base_X:
        X = [[0 for x in range(32)] for i in range(3)]
        y = [-1, 0, 1]
        clf.fit(X, y)
        return clf

    X = base_X
    y = base_y
    clf.fit(X, y)
    return clf


def get_random_change(value, percent):
    xd = random.choice([-1, 1])
    return (xd - value)*percent


def do_mutation(nn):
    for layer in range(2):
        arr = nn.coefs_[layer]
        for idx in random.sample(range(0, len(arr)-1), 3):
            arr[idx] += get_random_change(arr[idx], 0.2)


def do_crossover(C1, C2):
    genome1 = np.copy(C1)
    genome2 = np.copy(C2)
    for i in range(3):
        i = random.randint(0, len(C1[0]))
        j = random.randint(1, 10)
        r = slice(i,i+j)
        genome1[0][r], genome2[0][r] =  genome2[0][r],genome1[0][r]

    return genome1,genome2

def score_fitness(scenes):
    """Return score with an index [(s1, i1), (s2, i2), ...]"""
    return [(scene.get_score(), scene.score_layer.generation, i)  for i,scene in enumerate(scenes)]

class GeneticAlgo:
    def __init__(self, init_pop, main_scene,
        perform_mutation = do_mutation, perform_crossover = do_crossover,
        fitness = score_fitness):
        self.population = init_pop
        self.main_scene = main_scene
        self.nns = [make_nn() for i in range(self.population)]
        self.generation = 0
        self.perform_mutation = perform_mutation
        self.perform_crossover = perform_crossover
        self.fitness = fitness


    def predict(self, i, x):
        if not scaler:
            return self.nns[i].predict([x])[0]
        else:
            return self.nns[i].predict(scaler.transform([x]))[0]

    def do_crossover(self, i, j):
        return self.perform_crossover(self.nns[i].coefs_, self.nns[j].coefs_)


    def do_mutation(self, i):
        return self.perform_mutation(self.nns[i])


    def promote_nextgeneration(self):
        for scene in self.main_scene.scenes:
            scene.score_layer.generation += 1
            scene.score_layer.mutated += 1
            scene.score_layer.update_image()


    def add_generation(self):
        """Add new generation into the population where some of the dies"""
        self.generation += 1
        self.promote_nextgeneration()
        l = len(self.main_scene.scenes)
        ranking = self.fitness(self.main_scene.scenes)
        ranking.sort(reverse=True)
        gdp = sum([x[0] for x in ranking])
        print('#{} GDP={} Ranking={}'.format(self.generation, gdp, ranking))

        strong_idx = int(0.25 * l)
        middle_idx = int((0.25+0.25) * l)
        strong, middle, weak = [x[-1] for x in ranking[0:strong_idx]], [x[-1] for x in ranking[strong_idx:middle_idx]], [x[-1] for x in ranking[middle_idx:]]

        print(strong, middle, weak)
        strong_sample = random.sample(strong, 2)
        strong_breed = self.do_crossover(*strong_sample)
        middle_breed = self.do_crossover(strong[0], strong[-1])

        # print(strong_breed)
        # print(middle_breed)
        self.nns[weak[-1]].coefs_ = strong_breed[0]
        self.nns[weak[-2]].coefs_ = strong_breed[1]
        self.nns[weak[-3]].coefs_ = middle_breed[0]
        self.nns[weak[-4]].coefs_ = middle_breed[1]

        gens = [min([self.main_scene.scenes[x].score_layer.generation for x in strong_sample]),
            min([self.main_scene.scenes[x].score_layer.generation for x in [strong[0], strong[-1]]])]

        for i in weak[-4:]:
            self.main_scene.scenes[i].score_layer.generation = 0
            self.main_scene.scenes[i].score_layer.mutated = 0

        self.main_scene.scenes[weak[-1]].score_layer.generation = gens[0]+1
        self.main_scene.scenes[weak[-2]].score_layer.generation = gens[0]+1
        self.main_scene.scenes[weak[-3]].score_layer.generation = gens[1]
        self.main_scene.scenes[weak[-4]].score_layer.generation = gens[1]

        for i in weak[-4:]:
            self.main_scene.scenes[i].score_layer.update_image()

        # FIXME: Hardcoded value of 2
        for sample in range(len(self.main_scene.scenes)):
            self.do_mutation(sample)


    def old_add_generation(self):
        # retain 25% of the best fit Genomes
        self.generation += 1
        print('Generation {}'.format(self.generation))
        new_genration = []
        self.sorted_idx = self.sortedGeneration()
        L = self.sorted_idx
        # genomes to retain
        retain_counts = 5
        new_genration = [ self.nns[x[1]]  for x  in L[-5:]]

        ran = random.sample(xrange(0,14),3)
        ran_genration = [self.nns[x] for x in  ran ]
        new_genration.extend(ran_genration)

        # perform mutation
        z = random.sample(xrange(0,8),3)
        for x in z:
            self.do_mutation(new_genration[x])

        # perform crossover
        for x in range(6):
            i ,j = random.sample(xrange(0,19),2)
            C1,C2 = self.do_crossover(i,j)
            nnn1 = make_nn()
            nnn1.coefs_ = C1
            nnn2 = make_nn()
            nnn2.coefs_ = C2
            new_genration.append(nnn1)
            new_genration.append(nnn2)

        self.nns = new_genration
