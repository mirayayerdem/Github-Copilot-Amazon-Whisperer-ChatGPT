from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)
    # Calculate the range of the numbers
    range_num = max_num - min_num
    # Return the rescaled numbers
    return [(num - min_num) / range_num for num in numbers]
