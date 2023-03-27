from typing import List, Tuple


def foo(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> foo([])
    (0, 1)
    >>> foo([1, 2, 3, 4])
    (10, 24)
    """
    sum = 0
    product = 1
    for number in numbers:
        sum += number
        product *= number
    return (sum, product)
