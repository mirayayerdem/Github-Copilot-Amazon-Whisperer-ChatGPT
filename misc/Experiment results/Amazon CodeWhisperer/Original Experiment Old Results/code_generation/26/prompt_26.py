from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    result = []
    for i in range(len(numbers)):
        if numbers[i] not in numbers[:i] and numbers[i] not in numbers[i + 1:]:
            result.append(numbers[i])
    return result
