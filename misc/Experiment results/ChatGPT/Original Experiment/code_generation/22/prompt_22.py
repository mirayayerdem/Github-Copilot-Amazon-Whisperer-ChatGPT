from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    """
    # Use a list comprehension to filter the list of values for integers
    return [value for value in values if isinstance(value, int)]
