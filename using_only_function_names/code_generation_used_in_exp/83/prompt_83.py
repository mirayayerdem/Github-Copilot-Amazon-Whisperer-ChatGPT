
def starts_one_ends(n):
    """
    Returns True if the number starts with 1 and ends with 1.
    :param n: Number.
    :return: True if the number starts with 1 and ends with 1.
    """
    return n % 10 == 1 and n % 100 != 11
