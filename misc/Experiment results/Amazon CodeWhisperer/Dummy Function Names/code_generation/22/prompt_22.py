from typing import List, Any


def foo(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> foo(['a', 3.14, 5])
    [5]
    >>> foo([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]
