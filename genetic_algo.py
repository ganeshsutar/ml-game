from sklearn.neural_network import MLPClassifier

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

    def mutate(self):
        pass

    def crossover(self):
        pass

    def predict(self, i, x):
        return self.nns[i].predict([x])[0]

    def add_generation(self):
        crossover()
        mutate()
