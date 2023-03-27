
from typing import List

def foo(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> foo([1.0, 2.0, 3.0], 0.5)
    False
    >>> foo([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers.sort()
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) < threshold:
            return True
    return False


