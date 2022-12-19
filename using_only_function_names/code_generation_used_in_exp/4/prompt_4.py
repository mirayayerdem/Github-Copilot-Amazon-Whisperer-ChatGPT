from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculates the mean absolute deviation of a list of numbers.
    :param numbers: List of numbers.
    :return: Mean absolute deviation.
    """
    mean = sum(numbers) / len(numbers)
    deviations = [abs(number - mean) for number in numbers]
    return sum(deviations) / len(deviations)
