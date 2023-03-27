

def foo(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> foo([1, 2, 4, 20])
    True
    >>> foo([1, 20, 4, 10])
    False
    >>> foo([4, 1, 0, -10])
    True
    """
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    return increasing or decreasing
