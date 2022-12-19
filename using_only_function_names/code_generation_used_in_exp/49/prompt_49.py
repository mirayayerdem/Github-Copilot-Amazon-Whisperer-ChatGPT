

def modp(n: int, p: int):
    """
    Calculates the nth Fibonacci number.
    :param n: nth Fibonacci number.
    :param p: pth Fibonacci number.
    :return: nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return modp(n - 1, p) + modp(n - 2, p)
