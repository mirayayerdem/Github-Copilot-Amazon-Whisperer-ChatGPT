

def fib(n: int):
    """Return the nth Fibonacci number.
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
