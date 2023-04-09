from csv import reader
import os


NUMBER_OF_SAMPLES = 164


def calculate_dropped_validity_and_correctness(path):
    with open(path + "/comparison_results.csv", "r") as csvfile:
        reader = reader(csvfile)
        values = [[] for i in range(len(next(reader)))] # initialize empty lists for each column

        for row in reader:
            for i, value in enumerate(row):
                values[i].append(value)

        dropped_validity = 0
        dropped_correctness = 0
        
        for i in range(NUMBER_OF_SAMPLES):
            if values[0][i] <= values[2][i]:
                dropped_correctness = dropped_correctness + 1

            if values[1][i] <= values[3][i]:
                dropped_validity = dropped_validity + 1


        print("Dropped scores after removing the prompt part of problems:")
        print()
        print("Dropped validity percentage: ", float(dropped_validity) / float(164))
        print("Dropped correctness percentage: ", float(dropped_correctness) / float(164))


calculate_dropped_validity_and_correctness(os.getcwd())