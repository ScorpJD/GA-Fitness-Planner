class Fitness:
    # List of genes/exercises
    chromosome = []
    fitness_goal = ""

    def __init__(self, chromosome, fitness_goal):
        self.chromosome = chromosome
        self.fitness_goal = fitness_goal

    def calculate_fitness(self):
        cardio_exercise_count = 0
        total_exercise_count = len(self.chromosome)

        for gene in self.chromosome:
            # convert float to string to access first digit of encoded value
            encoded_val = str(gene[1])
            first_digit = encoded_val[0]

            if first_digit == "0":
                cardio_exercise_count += 1

        # divide num of cardio exercises by total num of exercises, round score to nearest hundredths place
        score = round(cardio_exercise_count / total_exercise_count, 2)

        # modify score according to the fitness goal
        if score < 0.5 and self.fitness_goal == "lose fat":
            score -= 1
        elif score >= 0.5 and self.fitness_goal == "lose fat":
            score += 1
        elif score < 0.5 and self.fitness_goal == "gain muscle":
            score += 1
        elif score >= 0.5 and self.fitness_goal == "gain muscle":
            score -= 1

        # set score tuple to be chromosome with a score
        chromosome_score = (self.chromosome, score)
        return chromosome_score