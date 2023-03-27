

def derivative(xs: list):
    """
    :param xs: list of numbers
    :return: list of derivative of xs
    """
    return [x * (x - 1) for x in xs]