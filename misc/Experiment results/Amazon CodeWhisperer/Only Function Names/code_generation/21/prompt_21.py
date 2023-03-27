from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescale a list of numbers to the unit interval.
    """
    return [x / max(numbers) for x in numbers]
