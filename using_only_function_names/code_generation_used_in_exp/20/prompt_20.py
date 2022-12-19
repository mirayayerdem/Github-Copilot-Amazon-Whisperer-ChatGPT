from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Finds the two closest elements in a list of numbers.
    :param numbers: List of numbers.
    :return: Tuple of the two closest numbers.
    """
    closest_elements = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if closest_elements is None or abs(numbers[i] - numbers[j]) < abs(closest_elements[0] - closest_elements[1]):
                closest_elements = (numbers[i], numbers[j])
    return closest_elements
