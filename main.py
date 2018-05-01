import csv
from csv_writer_util import CsvWriterUtil
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

    # List to store next generation of workouts
    next_gen_population = []

    # List to store best of each generation
    best_of_generations = []

    # Best overall workout
    best_overall_workout = []

    # Flag used to stop the GA from running
    has_found_best = False

    # Generate random number to init population between 2 and 10
    population_size = random.randrange(2, 10)

    while population_size % 2 != 0:
        # generate a new random number, population should be an even number of individuals
        population_size = random.randrange(2, 10)

    while not has_found_best:
        population = Population(pop_size=population_size)
        if current_generation_count == 1:
            # Initialize population for first generation using workout plans from file
            starting_population = population.init_population()
        else:
            # Initialize population with next generation
            starting_population = population.init_next_gen_population(next_gen_population=next_gen_population)
            # Reset next gen population list
            next_gen_population = []

        # score chromosomes in the population against fitness goal
        scored_population = []
        for chromosome in starting_population:
            fitness = Fitness(chromosome=chromosome, fitness_goal=fitness_goal)
            scored_chromosome = fitness.calculate_fitness()
            scored_population.append(scored_chromosome)


        # Select parents for offspring generation
        for ch in range(0, scored_population.__len__(), 1):
            # perform parent selection from scored population
            selection = Selection(population=scored_population)
            parents = selection.select()

            # perform crossover based on 50% probability
            crossover_prob = random.choice([True, False])
            crossover = Crossover(parents, crossover_probability=crossover_prob)
            offspring = crossover.perform_crossover()

            # perform mutation based on 50% probability
            mutation_prob = random.choice([True, False])
            mutation = Mutation(offspring, mutation_probability=mutation_prob)
            final_offspring = mutation.mutate()

            # add offspring to next generation
            next_gen_population.append(final_offspring)

        # Score next gen population
        scored_next_gen_population = []
        for chromosome in next_gen_population:
            fitness = Fitness(chromosome=chromosome, fitness_goal=fitness_goal)
            scored_next_gen_chromosome = fitness.calculate_fitness()
            scored_next_gen_population.append(scored_next_gen_chromosome)

        # Get generation best
        scored_next_gen_population.sort(key=lambda x: x[1])
        last_index = scored_next_gen_population.__len__() - 1
        best_of_generations.append(scored_next_gen_population[last_index])

        # Check to see if any chromosomes have scored 2.0, if so then stop the GA
        for workout in best_of_generations:
            workout_score = workout[1]
            if workout_score == 2.0:
                print("Best workout found in generation '" + str(current_generation_count) + "': " + str(workout))
                best_overall_workout.append(workout)
                has_found_best = True
                break
            else:
                # increase current generation count
                current_generation_count += 1

    # Print out the best of each generation
    for index, workout in enumerate(best_of_generations):
        print("Best for generation " + str(index) + ": " + str(workout))

    # Write the best to a csv file called best_workout.csv
    CsvWriterUtil.write_workout_to_file(self=CsvWriterUtil, workout=best_overall_workout)



