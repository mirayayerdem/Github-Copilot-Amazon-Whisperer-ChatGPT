from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Return a tuple of the sum and product of the numbers in the list.

    >>> sum_product([1, 2, 3])
    (6, 6)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum = 0
    product = 1
    for number in numbers:
        sum += number
        product *= number
    return (sum, product)