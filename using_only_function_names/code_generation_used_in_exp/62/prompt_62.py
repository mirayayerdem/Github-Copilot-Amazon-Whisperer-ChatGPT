

def derivative(xs: list):
    """
    Returns the derivative of a list of numbers.
    :param xs: List of numbers.
    :return: List of numbers.
    """
    return [x * (len(xs) - 1) for x in xs[1:]]
