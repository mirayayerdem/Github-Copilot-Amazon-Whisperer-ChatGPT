

def change_base(x: int, base: int):
    """
    Changes the base of a number.
    :param x: Number to change the base of.
    :param base: Base to change the number to.
    :return: Number in the new base.
    """
    if x < base:
        return x
    else:
        return change_base(x // base, base) + x % base
