from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """Remove duplicates from the list of numbers.
    
    >>> remove_duplicates([1, 2, 3])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1, 2])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1, 2, 3])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1, 2, 3, 1])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1, 2, 3, 1, 2])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1, 2, 3, 1, 2, 3])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1, 2, 3, 1, 2, 3, 1])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
    [1, 2, 3]
    """
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result
