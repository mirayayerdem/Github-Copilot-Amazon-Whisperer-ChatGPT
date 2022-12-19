

def foo(n: int):
    """
    foo returns n-th number that is a Fibonacci number and it's also prime.
    >>> foo(1)
    2
    >>> foo(2)
    3
    >>> foo(3)
    5
    >>> foo(4)
    13
    >>> foo(5)
    89
    """
    return fibonacci(n)


def fibonacci(n: int) -> int:
    """
    fibonacci returns n-th number that is a Fibonacci number.
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
