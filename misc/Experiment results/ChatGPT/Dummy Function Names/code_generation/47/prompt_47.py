

import statistics

def foo(l: list):
    """Return median of elements in the list l.
    >>> foo([3, 1, 2, 4, 5])
    3
    >>> foo([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(l)


