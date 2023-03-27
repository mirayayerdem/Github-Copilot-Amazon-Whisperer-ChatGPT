
def circular_shift(x, shift):
    """
    Circular shift of a list
    """
    return x[shift:] + x[:shift]
