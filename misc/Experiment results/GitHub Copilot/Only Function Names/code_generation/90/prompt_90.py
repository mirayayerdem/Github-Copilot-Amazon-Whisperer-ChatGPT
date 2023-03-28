
def next_smallest(lst):
    """ (list of int) -> int

    Return the next smallest number in lst that is not in lst.

    >>> next_smallest([1, 2, 3])
    4
    >>> next_smallest([5, 3, 1])
    2
    """
    i = 1
    while i in lst:
        i += 1
    return i