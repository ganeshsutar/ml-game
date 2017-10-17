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


    def do_crossover(self,i,j):
        C1,C2 = self.nns[i].coefs_,self.nns[j].coefs_
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
        # get indexes
        L  = self.sorted_idx
        i,j = L[-1][1],L[-2][1]
        C1,C2 = self.do_crossover(i,j)
        ri,rj = L[0][1], L[1][1]
        ## set
        self.nns[ri].coefs_ = C1
        self.nns[rj].coefs_ = C2

    def sortedGeneration(self):
        L= [ (scene.get_score(),i)  for i,scene in enumerate(self.main_scene.scenes)]
        self.sorted_idx = sorted(L)

    def predict(self, i, x):
        return self.nns[i].predict([x])[0]


    def add_generation(self):
        # retain 25% of the best fit Genomes
        new_genration = []
        self.sortedGeneration()
        L = self.sorted_idx
        # genomes to retain
        retain_counts = 5;
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
        print(len(self.nns))
