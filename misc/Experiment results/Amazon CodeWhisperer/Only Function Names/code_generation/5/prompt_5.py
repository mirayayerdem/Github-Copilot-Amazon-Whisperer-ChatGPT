from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Intersperse a delimeter between each element of a list of numbers.
    """
    result = []
    for i, num in enumerate(numbers):
        if i == 0:
            result.append(num)
        else:
            result.append(delimeter)
            result.append(num)
    return result
