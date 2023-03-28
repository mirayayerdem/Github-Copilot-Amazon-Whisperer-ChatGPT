
def is_sorted(lst):
    """ (list of int) -> bool

    Return True if and only if lst is sorted in non-decreasing order.

    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))