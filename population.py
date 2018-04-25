import random
import csv

class Population:
    # List of chromosomes
    population = []
    pop_size = 0

    def __init__(self, pop_size):
        self.pop_size = pop_size

    def init_population(self):
        if self.pop_size > 10 or self.pop_size % 2 != 0:
            raise ValueError(
                "Initial population size is greater than total possible population size or not an even number.")

        # List to store the starting population
        starting_population = []

        # Read the csv file to create chromosomes
        with open("workout_population.csv") as csvfile:
            readCSV = csv.reader(csvfile)
            current_plan_number = "1"
            chromosome = []
            for row in readCSV:
                if len(row[0]) > 1:
                    # skips adding csv column text to population
                    continue
                elif current_plan_number == row[0]:
                    # create gene tuple (exercise, encoded value)
                    gene = (row[1], float(row[4]))
                    # append this gene to the existing chromosome
                    chromosome.append(gene)
                else:
                    # chromosome is complete and needs to be added to init population
                    starting_population.append(chromosome)
                    # update the current plan number
                    current_plan_number = row[0]
                    # reset chromosome gene list for next chromosome
                    chromosome = []
                    # create gene tuple (exercise, encoded value)
                    gene = (row[1], float(row[4]))
                    # append current gene to new chromosome
                    chromosome.append(gene)

            # initialize population to specified population size
            self.population = random.sample(starting_population, self.pop_size)

        return self.population


    def init_next_gen_population(self, next_gen_population):
        self.population = next_gen_population
        return self.population

