def foo(l: list):
    """Return only positive numbers in the list.
    >>> foo([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> foo([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]

