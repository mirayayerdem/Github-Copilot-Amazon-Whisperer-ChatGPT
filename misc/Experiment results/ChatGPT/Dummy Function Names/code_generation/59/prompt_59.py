

def foo(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> foo(13195)
    29
    >>> foo(2048)
    2
    """
    largest_factor = 1
    while n % 2 == 0:
        largest_factor = 2
        n = n // 2
    for i in range(3, int(n**(1/2)) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n = n // i
    if n > 2:
        largest_factor = n
    return largest
