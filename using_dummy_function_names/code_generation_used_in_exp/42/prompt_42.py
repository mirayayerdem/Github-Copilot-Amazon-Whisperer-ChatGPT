

def foo(l: list):
    """Return list with elements incremented by 1.
    >>> foo([1, 2, 3])
    [2, 3, 4]
    >>> foo([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [v + 1 for v in l]
