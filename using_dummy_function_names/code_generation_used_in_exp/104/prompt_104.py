
def foo(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> foo([15, 33, 1422, 1])
    [1, 15, 33]
    >>> foo([152, 323, 1422, 10])
    []
    """
    return sorted(x for x in x if not any(int(d) % 2 == 0 for d in str(x)))
