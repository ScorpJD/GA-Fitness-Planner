import random

class Mutation:
    offspring = []
    mutation_probability = True

    def __init__(self, offspring, mutation_probability):
        self.offspring = offspring
        self.mutation_probability = mutation_probability

    def mutate(self):
        final_offspring = []
        if self.mutation_probability:
            print("Mutating offspring...")
            rand_mutation_val = random.randrange(-1, 1)
            print("Random mutation val: " + str(rand_mutation_val))
            for gene in self.offspring:
                encoded_val = gene[1]
                # split encoded value into two parts [ 0 or 1 , sets and reps ]
                encoded_val_by_parts = str(encoded_val).split(".")
                # get the sets and reps number out of the encoded_val_by_parts list
                set_rep_num_val = encoded_val_by_parts[1]
                # get sets number
                num_sets = int(set_rep_num_val[:2])
                # get reps number
                num_reps = int(set_rep_num_val[2:])

                # randomly mutate number of sets or number of reps
                mutate_sets = random.choice([True, False])
                if mutate_sets:
                    # mutate the number of sets
                    num_sets += rand_mutation_val
                else:
                    # mutate the number of reps
                    num_reps += rand_mutation_val

                # join encoded value parts back together
                num_sets_rep_str = "0" + str(num_sets) + str(num_reps)

                # create new encoded value
                new_encoded_val_str = str(encoded_val_by_parts[0]) + "." + num_sets_rep_str

                # convert to float
                new_encoded_val = float(new_encoded_val_str)

                # create new gene (exercise, new_encoded_val)
                new_gene = (gene[0], new_encoded_val)
                final_offspring.append(new_gene)
        else:
            # no mutation was performed
            final_offspring = self.offspring
        return final_offspring
