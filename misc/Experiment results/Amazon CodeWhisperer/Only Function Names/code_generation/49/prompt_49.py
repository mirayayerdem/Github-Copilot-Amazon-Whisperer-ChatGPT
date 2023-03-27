

def modp(n: int, p: int):
    """
    Modular multiplicative inverse.
    """
    return pow(n, p-2, p)