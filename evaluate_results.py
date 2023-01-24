import os
from csv import reader
#import experiment

NUMBER_OF_SAMPLES = 164


def calculate_correctness(path):
    # Read the csv file
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)
    # Calculate the correctess
    correctness = 0
    count = 0
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if  "N/A"  not in  matrix[i][1]:
            count += 1
            correctness += float(matrix[i][1])
    return float(correctness / NUMBER_OF_SAMPLES)


def calculate_different_correctness_cases(path):
    # Read the csv file
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    count_correct = 0
    count_incorrect = 0
    count_partially_correct = 0

    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if 'N/A' in matrix[i][1]:
            count_incorrect += 1
        else:
            if float(matrix[i][1]) == 1.0:
                count_correct += 1
            elif float(matrix[i][1]) == 0.0:
                count_incorrect += 1
            else:
                count_partially_correct += 1

    results = [count_correct, count_incorrect, count_partially_correct]

    return results


def calculate_correctness_by_percentage(path):
    # Read the csv file
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    # Calculate the correctness
    count_75_100 = 0
    count_50_75 = 0
    count_25_50 = 0
    count_0_25 = 0
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if not 'N/A' in matrix[i][1]:
            if 1 > float(matrix[i][1]) > 0.75:
                count_75_100 += 1
            elif 0.75 >= float(matrix[i][1]) > 0.5:
                count_50_75 += 1
            elif 0.5 >= float(matrix[i][1]) > 0.25:
                count_25_50 += 1
            elif 0.25 >= float(matrix[i][1]) > 0:
                count_0_25 += 1
    return [count_75_100, count_50_75, count_25_50, count_0_25]


def return_percentages_correctness(path):
    scores = calculate_correctness_by_percentage(path)
    scale_ratings = calculate_correctness_with_test_cases(path)

    percentages = []
    percentages_scale_ratings = []

    for i in range(len(scores)):
        percentages.append(float(scores[i] / sum(scores)))

    for i in range(len(scale_ratings)):
        percentages_scale_ratings.append(
            float(scale_ratings[i] / sum(scale_ratings)))

    return percentages, percentages_scale_ratings


def read_all_exec_results(path):
    results = []
    for i in range(0, NUMBER_OF_SAMPLES):
        with open(path + "/" + str(i) + "/output_correctness_validity.txt", "r") as f:
            content = f.read().splitlines()
            results.append(content[0])
    return results


def count_invalid(path):
    # Read the csv file
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)
    count = 0
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if '0' in matrix[i][2]:
            count += 1
    return count


def calculate_validity(path):
    count = count_invalid(path)
    return float((NUMBER_OF_SAMPLES - count) / NUMBER_OF_SAMPLES)

print()
print("Average Correctness with Invalid Generations:", calculate_correctness(os.getcwd()))
print()
different_correctness_cases = calculate_different_correctness_cases(os.getcwd())
print("Correct:", str(different_correctness_cases[0]), "Incorrect:", str(different_correctness_cases[1]), "Partially Correct:", str(different_correctness_cases[2]))
print()
correctness_by_percentage = calculate_correctness_by_percentage(os.getcwd())
print("100 > N > 75:", correctness_by_percentage[0], "\n75 >= N > 50:", correctness_by_percentage[1], "\n50 >= N > 25:", correctness_by_percentage[2], "\n25 >= N > 0:", correctness_by_percentage[3])
print()
print("Validity percentage:", calculate_validity(os.getcwd()))
print("Number of Invalid Generations:", count_invalid(os.getcwd()))