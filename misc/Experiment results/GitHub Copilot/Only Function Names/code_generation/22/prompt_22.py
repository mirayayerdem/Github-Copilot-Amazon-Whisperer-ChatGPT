from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Return a list of integers from the given list of values.
    
    >>> filter_integers([1, 2, 3])
    [1, 2, 3]
    >>> filter_integers([1, "2", 3])
    [1, 3]
    >>> filter_integers([1, "2", 3, "4"])
    [1, 3]
    >>> filter_integers([1, "2", 3, "4", 5])
    [1, 3, 5]
    """
    result = []
    for value in values:
        if type(value) == int:
            result.append(value)
    return result
