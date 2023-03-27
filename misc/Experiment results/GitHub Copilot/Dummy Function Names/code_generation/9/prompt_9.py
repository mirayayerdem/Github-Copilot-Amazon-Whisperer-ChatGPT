from typing import List, Tuple


def foo(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> foo([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max = None
    for number in numbers:
        if max is None or number > max:
            max = number
        result.append(max)
    return result
