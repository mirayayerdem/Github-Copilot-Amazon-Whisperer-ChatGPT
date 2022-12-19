import os
from csv import reader
import experiment

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
        if  "-1"  not in  matrix[i][1]:
            count += 1
            correctness += float(matrix[i][1])
    print("count: " + str(count))
    print("correctness: " + str(correctness))
    return float(correctness / count)


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
        if not '-1' in matrix[i][1]:
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


def calculate_correctness_with_test_cases(path):
    results = read_all_exec_results(path)
    test_numbers = experiment.count_test_cases(path)
    letter_results = [0, 0, 0, 0, 0]

    for i in range(0, NUMBER_OF_SAMPLES):
        if not 'Invalid' in results[i]:
            if float(results[i]) == float(test_numbers[i]):
                letter_results[0] += 1
            elif float(test_numbers[i]) > float(results[i]) >= float((3 * test_numbers[i]) / 4):
                letter_results[1] += 1
            elif float((3 * test_numbers[i]) / 4) > float(results[i]) >= float((test_numbers[i]) / 4):
                letter_results[2] += 1
            elif float((test_numbers[i]) / 4) >= float(results[i]) > 0:
                letter_results[3] += 1
            elif float(results[i]) == 0:
                letter_results[4] += 1
    return letter_results


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


def plot_no_of_test_cases(path):
    from matplotlib import pyplot as plt
    # import statistics library
    import statistics

    x = []
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        x.append(i)

    y = experiment.count_test_cases(path)

    # print the lowest and highest test cases
    print(min(y))
    print(max(y))

    # print the index of the minimum test
    print(y.index(min(y)))

    # calculate standard deviation for the test cases
    std_dev = statistics.stdev(y)
    print("Standard deviation: " + str(std_dev))

    # calculate mean for the test cases
    mean = statistics.mean(y)
    print("Mean: " + str(mean))

    # create a graph
    plt.plot(x, y)
    plt.xlabel("Sample")
    plt.ylabel("Number of test cases")
    plt.title("Number of test cases")
    plt.show()


print(calculate_correctness(os.getcwd()))
print(calculate_different_correctness_cases(os.getcwd()))
print(calculate_correctness_by_percentage(os.getcwd()))
# print(return_percentages_correctness(os.getcwd()))
print(count_invalid(os.getcwd()))
print(calculate_validity(os.getcwd()))
# print(calculate_correctness_with_test_cases(os.getcwd()))
# plot_no_of_test_cases(os.getcwd())
