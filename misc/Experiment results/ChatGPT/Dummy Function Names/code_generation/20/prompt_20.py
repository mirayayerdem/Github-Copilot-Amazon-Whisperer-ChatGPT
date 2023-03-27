from typing import List, Tuple

def foo(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> foo([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> foo([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    closest_diff = abs(numbers[1] - numbers[0])
    closest_pair = (numbers[0], numbers[1])
    for i in range(1, len(numbers) - 1):
        if abs(numbers[i+1] - numbers[i]) < closest_diff:
            closest_diff = abs(numbers[i+1] - numbers[i])
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair
