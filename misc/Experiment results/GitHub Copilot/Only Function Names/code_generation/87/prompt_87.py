
def get_row(lst, x):
    """ (list of list of int, int) -> list of int

    Precondition: 0 <= x < len(lst)

    Return row x from lst.

    >>> get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
    [4, 5, 6]
    """
    return lst[x]