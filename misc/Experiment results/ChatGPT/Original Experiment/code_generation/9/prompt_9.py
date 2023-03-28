from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    """
    max_so_far = 0
    result = []
    for number in numbers:
        max_so_far = max(max_so_far, number)
        result.append(max_so_far)
    return result
