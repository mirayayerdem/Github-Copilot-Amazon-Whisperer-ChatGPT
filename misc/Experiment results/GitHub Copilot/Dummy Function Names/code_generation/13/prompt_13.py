

def foo(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> foo(3, 5)
    1
    >>> foo(25, 15)
    5
    """
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return foo(a - b, b)
    return foo(a, b - a)
