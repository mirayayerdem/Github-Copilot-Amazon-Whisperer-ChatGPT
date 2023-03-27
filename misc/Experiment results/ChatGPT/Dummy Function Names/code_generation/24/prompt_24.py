def foo(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> foo(15)
    5
    """
    i = n-1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1
    return None
