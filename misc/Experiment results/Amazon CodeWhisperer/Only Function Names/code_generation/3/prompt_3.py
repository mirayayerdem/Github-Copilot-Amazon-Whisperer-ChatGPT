from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    >>> below_zero([1, -2, 3, -4, 5])
    False
    >>> below_zero([-1, -2, -3, -4, -5])
    True
    """
    return sum(operations) < 0
