class Selection:
    population = []
    parents = []

    def __init__(self, population):
        self.population = population
        self.parents = [None] * 2

    # sort population in order of score, least to greatest select best two according to fitness score (Rank selection)
    def select(self):
        self.population.sort(key=lambda x: x[1])
        if len(self.population) == 2:
            self.parents[0] = self.population[0]
            self.parents[1] = self.population[1]
        else:
            last_index = len(self.population) - 1
            second_last_index = last_index - 1
            self.parents[0] = self.population[last_index]
            self.parents[1] = self.population[second_last_index]
        return self.parents