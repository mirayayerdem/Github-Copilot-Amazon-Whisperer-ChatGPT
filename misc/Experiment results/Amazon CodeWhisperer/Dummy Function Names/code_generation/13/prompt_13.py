

def foo(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> foo(3, 5)
    1
    >>> foo(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a
