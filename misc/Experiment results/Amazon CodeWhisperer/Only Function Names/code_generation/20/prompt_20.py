from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the two elements in the given array that have the smallest absolute difference between them.
    """
    numbers.sort()
    return numbers[0], numbers[1]
