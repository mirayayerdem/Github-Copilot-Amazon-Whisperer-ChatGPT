
def closest_integer(value):
    """
    This function takes a floating point value and returns the closest integer
    to that value.
    """
    if value < 0:
        return int(value - 0.5)
    else:
        return int(value + 0.5)


