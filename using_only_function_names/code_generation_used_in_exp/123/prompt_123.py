
def get_odd_collatz(n):
    """
    Returns the odd collatz number of n.
    :param n: Number.
    :return: The odd collatz number of n.
    """
    return n // 2 if n % 2 == 1 else 3 * n + 1



