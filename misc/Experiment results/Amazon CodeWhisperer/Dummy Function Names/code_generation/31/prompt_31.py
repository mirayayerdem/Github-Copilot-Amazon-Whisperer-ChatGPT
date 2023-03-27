

def foo(n):
    """Return true if a given number is prime, and false otherwise.
    >>> foo(6)
    False
    >>> foo(101)
    True
    >>> foo(11)
    True
    >>> foo(13441)
    True
    >>> foo(61)
    True
    >>> foo(4)
    False
    >>> foo(1)
    False
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
