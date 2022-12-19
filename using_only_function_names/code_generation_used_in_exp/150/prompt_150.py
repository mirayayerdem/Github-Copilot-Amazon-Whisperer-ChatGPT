
def x_or_y(n, x, y):
    """
    Returns the value of x or y, whichever is smaller.
    :param n: The value of n.
    :param x: The value of x.
    :param y: The value of y.
    :return: The value of x or y, whichever is smaller.
    """
    if n % x == 0:
        return x
    elif n % y == 0:
        return y
    else:
        return n

