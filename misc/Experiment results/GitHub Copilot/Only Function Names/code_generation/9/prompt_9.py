from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list of the maximum value of the rolling window of size 3.
    
    >>> rolling_max([1, 2, 3, 4, 5])
    [3, 4, 5]
    >>> rolling_max([1, 2, 3, 4, 5, 6])
    [3, 4, 5, 6]
    >>> rolling_max([1, 2, 3, 4, 5, 6, 7])
    [3, 4, 5, 6, 7]
    """
    result = []
    for i in range(len(numbers)):
        if i < 2:
            continue
        result.append(max(numbers[i - 2], numbers[i - 1], numbers[i]))
    return result