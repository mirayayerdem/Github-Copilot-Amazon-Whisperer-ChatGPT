

def triples_sum_to_zero(l: list):
    """
    Returns a list of triples that sum to zero.
    :param l: List of numbers.
    :return: List of triples that sum to zero.
    """
    return [(x, y, z) for x in l for y in l for z in l if x + y + z == 0]

