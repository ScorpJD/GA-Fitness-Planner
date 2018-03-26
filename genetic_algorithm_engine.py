class GeneticAlgorithmEngine:
    population = []
    generation_runs = 1

    def __init__(self, population, generation_runs):
        self.population = population
        self.generation_runs = generation_runs