import csv

class CsvWriterUtil:

    # workout data structure: (exercises, fitness_score)
    # exercises data structure: [(exercise_name, set_rep_encoded_val), (exercise_name, set_rep_encoded_val)), ...]
    def write_workout_to_file(self, workout):
        workout_plan = workout[0][0]
        print("Writing workout to file 'best_workout.csv'...")
        with open("best_workout.csv", 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Exercise', 'Sets', 'Reps'])

            for exercise in workout_plan:
                exercise_name = exercise[0]
                sets_reps = exercise[1]
                # split sets/rep encoded value
                sets_reps_split = str(sets_reps).split('.')
                # parse sets and reps from encoded val string
                sets = int(sets_reps_split[1][:2])
                reps = int(sets_reps_split[1][2:])
                csv_writer.writerow([exercise_name, str(sets), str(reps)])
