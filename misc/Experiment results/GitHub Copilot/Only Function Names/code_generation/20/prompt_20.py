from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Return a tuple of the two closest elements in the list.
    
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
    (1.0, 2.0)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    (1.0, 2.0)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    (1.0, 2.0)
    """
    closest = (numbers[0], numbers[1])
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if abs(numbers[i] - numbers[j]) < abs(closest[0] - closest[1]):
                closest = (numbers[i], numbers[j])
    return closest