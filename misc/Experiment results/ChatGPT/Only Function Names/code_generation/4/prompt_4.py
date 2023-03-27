from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(number - mean) for number in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)

