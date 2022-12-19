

def foo(l):
    """
    foo takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> foo([1, 3, 5, 0])
    False
    >>> foo([1, 3, -2, 1])
    False
    >>> foo([1, 2, 3, 7])
    False
    >>> foo([2, 4, -5, 3, 5, 7])
    True
    >>> foo([1])
    False
    """
    return any(sum(x) == 0 for x in combinations(l, 2))
