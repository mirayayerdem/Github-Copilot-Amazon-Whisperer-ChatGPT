from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    >>> sum_product([1, 2, 3])
    (6, 3)
    >>> sum_product([1, 2, 3, 4, 5])
    (120, 15)
    """
    return sum(numbers), reduce(lambda x, y: x * y, numbers)
