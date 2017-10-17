from sklearn.neural_network import MLPClassifier
import numpy as np
import random
def make_nn():
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5), random_state=None)
    X = [[0 for x in range(32)] for i in range(3)]
    y = [-1, 0, 1]
    clf.fit(X, y)
    return clf


class GeneticAlgo:
    def __init__(self, init_pop, main_scene):
        self.population = init_pop
        self.main_scene = main_scene
        self.nns = [make_nn() for i in range(self.population)]


    def do_mutation(self, nn):
        layer = random.randint(0, 1)
        arr = nn.coefs_[layer]
        idx = random.randint(0, len(arr)-1)
        change = arr[idx] * 0.1
        add_minus = random.randint(0,1)
        if add_minus == 0:
            arr[idx] += change
        else:
            arr[idx] -= change


    def mutate(self):
        i = random.randint(0, len(self.nns)-1)
        nn = self.nns[i]
        self.do_mutation(nn)


    def do_crossover(self,C1,C2):
        genome1 = np.copy(C1)
        genome2 = np.copy(C2)
        i = random.randint(0, len(C1[0]))
        j = random.randint(1, 10)
        r = slice(i,i+j)
        genome1[0][r], genome2[0][r] =  genome2[0][r],genome1[0][r]

        i = random.randint(0, len(C1[1]))
        j = random.randint(1, 3)
        x = slice(i,i+j)
        genome1[1][x], genome2[1][x] =  genome2[1][x],genome1[1][x]

        return genome1,genome2


    def crossover(self):
        L = [ (scene.get_score(),i)  for i,scene in enumerate(self.main_scene.scenes)]
        sorted(L)
        # get indexes
        i,j = L[-1][1],L[-2][1]
        C1,C2 = self.do_crossover(self.nns[i].coefs_,self.nns[j].coefs_)
        ri,rj = L[0][1], L[1][1]
        ## set
        self.nns[ri].coefs_ = C1
        self.nns[rj].coefs_ = C2


    def predict(self, i, x):
        return self.nns[i].predict([x])[0]


    def add_generation(self):
        self.crossover()
        if random.randint(0, 1) == 0:
            self.mutate()
