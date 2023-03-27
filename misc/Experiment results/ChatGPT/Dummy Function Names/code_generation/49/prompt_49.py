

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
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
        if n > 0:
            result = (result * result) % p
    return result
