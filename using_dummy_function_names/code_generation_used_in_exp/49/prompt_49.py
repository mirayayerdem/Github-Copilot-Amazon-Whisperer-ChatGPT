

def foo(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> foo(3, 5)
    3
    >>> foo(1101, 101)
    2
    >>> foo(0, 101)
    1
    >>> foo(3, 11)
    8
    >>> foo(100, 101)
    1
    """
    return 2 ** n % p
