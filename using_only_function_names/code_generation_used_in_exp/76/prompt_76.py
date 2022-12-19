
def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n.
    :param x: Number.
    :param n: Number.
    :return: True if x is a simple power of n.
    """
    return x == n ** (x // n)
