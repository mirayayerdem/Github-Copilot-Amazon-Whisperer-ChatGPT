

def foo(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> foo([1, 2, 4, 10], 100)
    True
    >>> foo([1, 20, 4, 10], 5)
    False
    """
    return all(v < t for v in l)
