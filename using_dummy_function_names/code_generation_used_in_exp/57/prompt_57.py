

def foo(l: list):
    """Return True is list elements are fooally increasing or decreasing.
    >>> foo([1, 2, 4, 20])
    True
    >>> foo([1, 20, 4, 10])
    False
    >>> foo([4, 1, 0, -10])
    True
    """
    return all(v < v1 for v, v1 in zip(l, l[1:])) or all(v > v1 for v, v1 in zip(l, l[1:]))
