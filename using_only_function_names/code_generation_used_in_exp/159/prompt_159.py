
def eat(number, need, remaining):
    """
    Returns the number of times the number of remaining units can be eaten.
    :param number: Number.
    :param need: Number.
    :param remaining: Number.
    :return: The number of times the number of remaining units can be eaten.
    """
    return number // need if number // need <= remaining else remaining

