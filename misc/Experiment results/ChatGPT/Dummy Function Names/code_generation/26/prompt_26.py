from typing import List

def foo(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> foo([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an empty set to store unique integers
    unique_numbers = set()
    # Create an empty list to store unique integers in the original order
    result = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.add(number)
            result.append(number)
    return result
