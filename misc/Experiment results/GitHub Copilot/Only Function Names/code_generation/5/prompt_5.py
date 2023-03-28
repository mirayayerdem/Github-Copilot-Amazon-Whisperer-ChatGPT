from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Intersperse the delimeter between each number in the list.

    >>> intersperse([1, 2, 3], 0)
    [1, 0, 2, 0, 3]
    >>> intersperse([1, 2, 3], 1)
    [1, 1, 2, 1, 3]
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result
