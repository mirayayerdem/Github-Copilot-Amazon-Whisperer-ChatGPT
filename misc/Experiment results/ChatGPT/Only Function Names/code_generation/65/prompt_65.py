
def circular_shift(x, shift):
    shift %= len(x)
    return x[-shift:] + x[:-shift]
