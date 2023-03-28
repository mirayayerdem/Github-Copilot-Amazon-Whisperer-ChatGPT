from typing import List


def sort_numbers(numbers: str) -> str:
    """Return the numbers sorted in ascending order.
    
    >>> sort_numbers("1, 2, 3")
    '1, 2, 3'
    >>> sort_numbers("3, 2, 1")
    '1, 2, 3'
    >>> sort_numbers("1, 3, 2")
    '1, 2, 3'
    >>> sort_numbers("1, 1, 1")
    '1, 1, 1'
    >>> sort_numbers("1, 2, 3, 4, 5")
    '1, 2, 3, 4, 5'
    >>> sort_numbers("5, 4, 3, 2, 1")
    '1, 2, 3, 4, 5'
    >>> sort_numbers("1, 2, 3, 4, 5, 6, 7, 8, 9")
    '1, 2, 3, 4, 5, 6, 7, 8, 9'
    >>> sort_numbers("9, 8, 7, 6, 5, 4, 3, 2, 1")
    '1, 2, 3, 4, 5, 6, 7, 8, 9'
    """
    numbers = numbers.split(", ")
    numbers = [int(number) for number in numbers]
    numbers.sort()
    numbers = [str(number) for number in numbers]
    return ", ".join(numbers)