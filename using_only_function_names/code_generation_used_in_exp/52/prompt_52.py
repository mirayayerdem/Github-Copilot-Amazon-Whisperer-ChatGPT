

def below_threshold(l: list, t: int):
    """
    Returns a list of elements below a threshold.
    :param l: List of numbers.
    :param t: Threshold.
    :return: List of numbers below the threshold.
    """
    return [x for x in l if x < t]
