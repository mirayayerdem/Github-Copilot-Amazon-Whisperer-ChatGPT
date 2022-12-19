
def special_factorial(n):
    """
    Returns the factorial of n, but only if n is even.
    :param n: Number.
    :return: The factorial of n, but only if n is even.
    """
    if n % 2 == 0:
        return factorial(n)
    else:
        return 0

def factorial(n):
    """
    Returns the factorial of n.
    :param n: Number.
    :return: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


