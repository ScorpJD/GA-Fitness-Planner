class Crossover:
    parents = []
    crossover_probability = True

    def __init__(self, parents, crossover_probability):
        self.parents = parents
        self.crossover_probability = crossover_probability

