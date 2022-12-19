

def fib(n: int):
    """
    Calculates the nth Fibonacci number.
    :param n: nth Fibonacci number.
    :return: nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
