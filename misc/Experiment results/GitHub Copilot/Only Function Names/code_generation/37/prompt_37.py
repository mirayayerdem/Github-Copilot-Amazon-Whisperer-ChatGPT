

def sort_even(l: list):
    """Sort the list in ascending order, but put the even numbers first.
    
    >>> sort_even([1, 2, 3, 4])
    [2, 4, 1, 3]
    >>> sort_even([1, 3, 5, 7])
    [1, 3, 5, 7]
    >>> sort_even([2, 4, 6, 8])
    [2, 4, 6, 8]
    >>> sort_even([2, 4, 1, 3, 5, 7])
    [2, 4, 1, 3, 5, 7]
    >>> sort_even([1, 3, 2, 4, 5, 7])
    [2, 4, 1, 3, 5, 7]
    >>> sort_even([1, 3, 5, 7, 2, 4])
    [2, 4, 1, 3, 5, 7]
    >>> sort_even([1, 3, 5, 7, 4, 2])
    [2, 4, 1, 3, 5, 7]
    """
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort()
    return even + odd
