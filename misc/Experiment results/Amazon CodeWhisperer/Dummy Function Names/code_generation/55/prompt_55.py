

def foo(n: int):
    """Return n-th Fibonacci number.
    >>> foo(10)
    55
    >>> foo(1)
    1
    >>> foo(8)
    21
    """
    if n <= 1:
        return n
    else:
        return foo(n-1) + foo(n-2)
