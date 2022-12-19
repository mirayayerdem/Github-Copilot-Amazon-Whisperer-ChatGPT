

def foo(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> foo(15)
    5
    """
    for i in range(n):
        if n % i == 0:
            return i
    return 0
