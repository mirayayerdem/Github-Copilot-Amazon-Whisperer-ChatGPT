from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter out non-integers from a list of values.
    """
    return [value for value in values if isinstance(value, int)]
