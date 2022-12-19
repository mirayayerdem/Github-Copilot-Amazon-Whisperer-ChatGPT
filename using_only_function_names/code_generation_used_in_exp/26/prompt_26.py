from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Removes duplicates from a list of numbers.
    :param numbers: List of numbers.
    :return: List of numbers without duplicates.
    """
    return list(set(numbers))
