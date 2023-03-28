
def largest_smallest_integers(lst):
    """ (list of int) -> tuple of (int, int)
    Return a tuple containing the largest and smallest integers in lst.
    >>> largest_smallest_integers([3, 7, -2, 12])
    (12, -2)
    """
    return (max(lst), min(lst))