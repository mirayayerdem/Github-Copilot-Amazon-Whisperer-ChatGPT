
def unique_digits(x):
    """
    Returns True if x has unique digits.
    :param x: Number.
    :return: True if x has unique digits.
    """
    return len(set(str(x))) == len(str(x))

