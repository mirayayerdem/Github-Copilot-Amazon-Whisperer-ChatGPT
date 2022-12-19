from typing import List


def foo(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> foo([], 4)
    []
    >>> foo([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    return [numbers[i] + delimeter if i < len(numbers) - 1 else numbers[i] for i in range(len(numbers))]
