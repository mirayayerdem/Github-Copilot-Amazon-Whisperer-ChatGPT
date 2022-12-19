
def choose_num(x, y):
    """
    Returns x choose y.
    :param x: Number.
    :param y: Number.
    :return: x choose y.
    """
    return factorial(x) // (factorial(y) * factorial(x - y))

def factorial(x):
    """
    Returns x!
    :param x: Number.
    :return: x!
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

