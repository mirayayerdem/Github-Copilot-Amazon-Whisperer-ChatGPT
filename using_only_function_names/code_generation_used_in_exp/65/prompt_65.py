
def circular_shift(x, shift):
    """
    Circularly shifts a list by a given amount.
    :param x: List of numbers.
    :param shift: Amount to shift.
    :return: Shifted list.
    """
    return x[shift:] + x[:shift]
