

def foo(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> foo(13195)
    29
    >>> foo(2048)
    2
    """
    for i in range(2, n):
        if n % i == 0:
            return foo(n // i)
    return n
