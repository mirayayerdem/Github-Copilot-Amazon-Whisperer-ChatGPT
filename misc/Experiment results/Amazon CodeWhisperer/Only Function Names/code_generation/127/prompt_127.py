
def intersection(interval1, interval2):
    """ (list) -> bool

    Return True if lst is sorted in non-decreasing order.

    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True


