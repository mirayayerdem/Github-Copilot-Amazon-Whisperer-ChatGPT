from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the mean absolute deviation of a list of numbers.

    :param numbers: list of numbers
    :return: mean absolute deviation
    """
    return sum(abs(x - sum(numbers) / len(numbers))) / len(numbers)