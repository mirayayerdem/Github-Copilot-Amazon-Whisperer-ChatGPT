
def get_max_triples(n):
    """
    Returns the maximum number of triples that can be formed from the digits of
    n.
    :param n: Number.
    :return: The maximum number of triples that can be formed from the digits
    of n.
    """
    return n * (n + 1) // 2

