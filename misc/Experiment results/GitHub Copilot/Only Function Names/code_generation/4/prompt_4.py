from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    >>> mean_absolute_deviation([1, 2, 3])
    0.6666666666666666
    >>> mean_absolute_deviation([1, 2, 3, 4])
    1.0
    >>> mean_absolute_deviation([1, 2, 3, 4, 5])
    1.2
    >>> mean_absolute_deviation([1, 2, 3, 4, 5, 6])
    1.5
    >>> mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7])
    1.7142857142857142
    >>> mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8])
    2.0
    >>> mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9])
    2.2222222222222223
    >>> mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    2.5
    """
    # BEGIN PROBLEM 1
    total = 0
    for i in range(len(numbers)):
        total += abs(numbers[i] - sum(numbers) / len(numbers))
    return total / len(numbers)
    # END PROBLEM 1