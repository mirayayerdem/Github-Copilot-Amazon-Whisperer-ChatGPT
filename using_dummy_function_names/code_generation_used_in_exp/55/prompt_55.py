

def foo(n: int):
    """Return n-th Fibonacci number.
    >>> foo(10)
    55
    >>> foo(1)
    1
    >>> foo(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return foo(n - 1) + foo(n - 2) + foo(n - 3) + foo(n - 4)
