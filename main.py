import csv
import random
from population import Population
from fitness import Fitness
from selection import Selection
from crossover import Crossover
from mutation import Mutation

#
# Developed by: Leo Espinal
# CS 767 Machine Learning
# GA Fitness Planner
#

# Run Genetic Algorithm loop
if __name__ == '__main__':
    # Store the individual's fitness goal
    fitness_goal = None
    while fitness_goal != "lose fat" and fitness_goal != "gain muscle":
        fitness_goal = input("Enter your fitness goal (lose fat or gain muscle): ")

    # init generation counter
    current_generation_count = 1

    # Generate random number of generations to run GA
    max_generation_count = random.randrange(1, 20, 1)

    # list to store next generation of workouts
    next_gen_population = []

    # Generate random number to init population between 2 and 10
    population_size = random.randrange(2, 10)

    while population_size % 2 != 0:
        # generate a new random number
        population_size = random.randrange(2, 10)

    while current_generation_count <= max_generation_count:
        population = Population(pop_size=population_size)
        if current_generation_count == 1:
            # Initialize population for first generation using workout plans from file
            starting_population = population.init_population()
        else:
            # Initialize population with next generation
            #starting_population = population.init_next_gen_population(next_gen_population=next_gen_population)
            print("TODO: Fix above commented code.")

        # score chromosomes in the population against fitness goal
        scored_population = []
        for chromosome in starting_population:
            fitness = Fitness(chromosome=chromosome, fitness_goal=fitness_goal)
            scored_chromosome = fitness.calculate_fitness()
            scored_population.append(scored_chromosome)

        for scored in scored_population:
            print("Scored chromosome: ")
            print(scored)

        # perform parent selection from scored population
        selection = Selection(population=scored_population)
        parents = selection.select()

        for parent in parents:
            print("Parent: ")
            print(parent)

        # increase current generation count
        current_generation_count += 1

