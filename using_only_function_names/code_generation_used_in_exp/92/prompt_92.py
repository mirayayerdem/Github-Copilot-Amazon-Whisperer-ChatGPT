
def any_int(x, y, z):
    """
    Returns the first non-negative integer that is a multiple of x, y, and z.
    :param x: First number.
    :param y: Second number.
    :param z: Third number.
    :return: First non-negative integer that is a multiple of x, y, and z.
    """
    for i in range(1, 100):
        if i % x == 0 and i % y == 0 and i % z == 0:
            return i
    return None

  

