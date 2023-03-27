from typing import List


def foo(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> foo([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
