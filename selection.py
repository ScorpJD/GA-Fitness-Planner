import random

class Selection:
    population = []
    parents = []
    parent = []

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

    # Roulette wheel selection
    # def select(self):
    #     # Sum up the fitness scores of all chromosomes in population
    #     total_pop_score = 0.0
    #     for index, (chromosome, fitness_score) in enumerate(self.population):
    #         total_pop_score += fitness_score
    #
    #     # Generate a random number between 0 - total_population_score
    #     if total_pop_score <= 0 or total_pop_score < 5.0:
    #         total_pop_score += 2.0
    #     rand_num = random.randrange(0, int(total_pop_score))
    #
    #     # Compute running sum of fitness scores in population and check against rand_num
    #     sum_so_far = 0.0
    #     for index, (chromosome, fitness_score) in enumerate(self.population):
    #         if sum_so_far > rand_num:
    #             # select this chromosome to be the parent
    #             self.parent.append(self.population[index])
    #             break
    #         else:
    #             # add this chromosome's fitness score to the running sum
    #             sum_so_far += fitness_score
    #
    #     if len(self.parent) != 1:
    #         random_selection_index = random.randrange(0, len(self.population) - 1)
    #         self.parent.append(self.population[random_selection_index])
    #
    #     return self.parent