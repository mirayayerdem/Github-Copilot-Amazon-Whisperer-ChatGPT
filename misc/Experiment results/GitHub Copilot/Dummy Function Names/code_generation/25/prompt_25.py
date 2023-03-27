from typing import List


def foo(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> foo(8)
    [2, 2, 2]
    >>> foo(25)
    [5, 5]
    >>> foo(70)
    [2, 5, 7]
    """
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors
