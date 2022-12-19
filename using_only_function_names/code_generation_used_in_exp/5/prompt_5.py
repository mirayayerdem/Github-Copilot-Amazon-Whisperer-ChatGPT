from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Interleaves a list of numbers with a delimiter.
    :param numbers: List of numbers.
    :param delimeter: Delimiter.
    :return: Interleaved list of numbers.
    """
    interleaved = []
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            interleaved.append(numbers[i])
        else:
            interleaved.append(numbers[i])
            interleaved.append(delimeter)
    return interleaved
