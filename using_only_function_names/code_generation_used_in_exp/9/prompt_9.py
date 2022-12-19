from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates the rolling max of a list of numbers.
    :param numbers: List of numbers.
    :return: List of rolling max.
    """
    rolling_max = []
    for i in range(len(numbers)):
        if i == 0:
            rolling_max.append(numbers[i])
        else:
            if numbers[i] > rolling_max[i - 1]:
                rolling_max.append(numbers[i])
            else:
                rolling_max.append(rolling_max[i - 1])
    return rolling_max
