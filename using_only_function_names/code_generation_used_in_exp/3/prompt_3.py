from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Check if the list of operations contains a negative number.
    :param operations: List of operations.
    :return: True if the list contains a negative number, False otherwise.
    """
    for operation in operations:
        if operation < 0:
            return True
    return False
