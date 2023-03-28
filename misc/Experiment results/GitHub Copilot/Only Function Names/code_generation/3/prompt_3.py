from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, -2, 3])
    True
    >>> below_zero([1, 2, -3])
    True
    >>> below_zero([-1, 2, 3])
    True
    >>> below_zero([1, -2, -3])
    True
    >>> below_zero([-1, 2, -3])
    True
    >>> below_zero([-1, -2, 3])
    True
    >>> below_zero([-1, -2, -3])
    True
    """
    # BEGIN PROBLEM 1
    for i in range(len(operations)):
        if operations[i] < 0:
            return True
    return False
    # END PROBLEM 1