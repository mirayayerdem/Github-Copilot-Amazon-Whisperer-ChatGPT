

def pairs_sum_to_zero(l):
    """
    Returns a list of pairs that sum to zero.
    :param l: List of numbers.
    :return: List of pairs that sum to zero.
    """
    return [(x, y) for x in l for y in l if x + y == 0]
