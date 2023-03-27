from typing import List


def foo(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> foo([], 4)
    []
    >>> foo([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for number in numbers:
        result.append(number)
        result.append(delimeter)
    return result[:-1]
