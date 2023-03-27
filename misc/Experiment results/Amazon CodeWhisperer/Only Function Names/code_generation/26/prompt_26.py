from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of numbers.
    """
    return list(set(numbers))
