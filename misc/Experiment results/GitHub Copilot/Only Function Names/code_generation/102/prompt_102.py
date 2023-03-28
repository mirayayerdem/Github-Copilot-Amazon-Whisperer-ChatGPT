
def choose_num(x, y):
    """ (int, int) -> int
    Return the smaller of x and y.
    >>> choose_num(3, 5)
    3
    >>> choose_num(5, 3)
    3
    """
    if x < y:
        return x
    else:
        return y