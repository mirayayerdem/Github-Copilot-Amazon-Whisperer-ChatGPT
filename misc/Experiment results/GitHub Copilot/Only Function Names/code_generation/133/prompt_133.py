

def sum_squares(lst):
    """ (list of int) -> int
    Return the sum of the squares of the elements in lst.
    >>> sum_squares([2, 3, 4])
    29
    >>> sum_squares([ ])
    0
    """
    return sum(i**2 for i in lst)