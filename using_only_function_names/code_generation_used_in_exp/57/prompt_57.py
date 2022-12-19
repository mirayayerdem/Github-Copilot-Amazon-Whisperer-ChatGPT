

def monotonic(l: list):
    """
    Returns True if the list is monotonic.
    :param l: List of numbers.
    :return: True if the list is monotonic.
    """
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))
