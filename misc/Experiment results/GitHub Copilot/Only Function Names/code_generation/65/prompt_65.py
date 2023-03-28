
def circular_shift(x, shift):
    return (x << shift) | (x >> (32 - shift))