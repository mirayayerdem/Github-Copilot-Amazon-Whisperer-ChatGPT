

def change_base(x: int, base: int):
    """
    :param x: int
    :param base: int
    :return: int
    """
    if x == 0:
        return 0
    else:
        return (x % base) + 10 * change_base(x // base, base)
