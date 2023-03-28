from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Return a list of numbers rescaled to be between 0 and 1.
    
    >>> rescale_to_unit([1.0, 2.0, 3.0])
    [0.0, 0.5, 1.0]
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0])
    [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number
    numbers = [(number - min) / (max - min) for number in numbers]
    return numbers
