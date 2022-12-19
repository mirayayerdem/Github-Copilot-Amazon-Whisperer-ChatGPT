from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescales a list of numbers to unit.
    :param numbers: List of numbers.
    :return: List of rescaled numbers.
    """
    min_value = min(numbers)
    max_value = max(numbers)
    return [((number - min_value) / (max_value - min_value)) for number in numbers]
