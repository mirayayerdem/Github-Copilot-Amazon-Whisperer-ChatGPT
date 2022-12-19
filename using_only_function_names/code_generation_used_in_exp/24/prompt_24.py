

def largest_divisor(n: int) -> int:
    """
    Calculates the largest divisor of n.
    :param n: Number to calculate the largest divisor of.
    :return: Largest divisor of n.
    """
    if n == 1:
        return 1
    else:
        return largest_divisor(n - 1)
