

def foo(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> foo([1, 2, 4, 20])
    True
    >>> foo([1, 20, 4, 10])
    False
    >>> foo([4, 1, 0, -10])
    True
    """
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))
