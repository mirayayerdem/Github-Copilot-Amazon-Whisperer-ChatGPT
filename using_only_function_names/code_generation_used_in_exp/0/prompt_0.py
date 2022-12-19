from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks if the list of numbers contains two close elements.

    :param numbers: List of numbers.
    :param threshold: Threshold value.
    :return: True if the list contains two close elements, False otherwise.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
