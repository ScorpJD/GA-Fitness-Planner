import random

class Crossover:
    parents = []
    crossover_probability = True

    def __init__(self, parents, crossover_probability):
        self.parents = parents
        self.crossover_probability = crossover_probability

    def perform_crossover(self):
        offspring = []
        if self.crossover_probability:
            # crossover point at parent A (the highest scoring chromosome)
            # if chromosome len = 3, range will be from 0 - 1 indicating index in list to copy
            len_parent_A = len(self.parents[0][0])
            crossover_point = random.randrange(0, len_parent_A - 2)
            parent_A = self.parents[0][0]
            parent_B = self.parents[1][0]

            # get genes from parent_A up til crossover point
            if crossover_point == 0:
                offspring.append(parent_A[0])
            else:
                for index in range(crossover_point):
                    offspring.append(parent_A[index])

            # get rest of genes from parent_B
            after_crossover_point = crossover_point + 1
            for i in range(after_crossover_point, len(parent_B)):
                offspring.append(parent_B[i])
        else:
            # make offspring the exact copy of parent_A since it is the highest scoring chromosome
            offspring = self.parents[0][0]
        return offspring