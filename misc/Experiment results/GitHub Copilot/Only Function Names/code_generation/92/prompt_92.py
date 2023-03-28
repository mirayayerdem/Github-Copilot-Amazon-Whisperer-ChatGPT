
def any_int(x, y, z):
    """ (int, int, int) -> bool

    Return True if at least one of x, y, and z is even and False otherwise.

    >>> any_int(2, 3, 4)
    True
    >>> any_int(1, 3, 5)
    False
    """
    return x % 2 == 0 or y % 2 == 0 or z % 2 == 0