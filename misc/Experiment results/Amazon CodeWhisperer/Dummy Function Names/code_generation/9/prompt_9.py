from typing import List, Tuple


def foo(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> foo([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    for i in range(len(numbers)):
        max_list.append(max(numbers[:i + 1]))
    return max_list
