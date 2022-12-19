
def simplify(x, n):
    """
    Simplifies the fraction x/n.
    :param x: Numerator.
    :param n: Denominator.
    :return: The simplified fraction.
    """
    if x % n == 0:
        return x // n
    else:
        return x, n


