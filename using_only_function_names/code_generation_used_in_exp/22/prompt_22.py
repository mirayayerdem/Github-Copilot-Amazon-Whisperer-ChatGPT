from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filters a list of values to only contain integers.
    :param values: List of values.
    :return: List of integers.
    """
    return [value for value in values if isinstance(value, int)]
