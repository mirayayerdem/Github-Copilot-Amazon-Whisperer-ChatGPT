from typing import List


def factorize(n: int) -> List[int]:
    """Return a list of the prime factors of n.

    >>> factorize(1)
    []
    >>> factorize(2)
    [2]
    >>> factorize(3)
    [3]
    >>> factorize(4)
    [2, 2]
    >>> factorize(5)
    [5]
    >>> factorize(6)
    [2, 3]
    >>> factorize(7)
    [7]
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(9)
    [3, 3]
    >>> factorize(10)
    [2, 5]
    >>> factorize(11)
    [11]
    >>> factorize(12)
    [2, 2, 3]
    >>> factorize(13)
    [13]
    >>> factorize(14)
    [2, 7]
    >>> factorize(15)
    [3, 5]
    >>> factorize(16)
    [2, 2, 2, 2]
    >>> factorize(17)
    [17]
    >>> factorize(18)
    [2, 3, 3]
    >>> factorize(19)
    [19]
    >>> factorize(20)
    [2, 2, 5]
    >>> factorize(21)
    [3, 7]
    >>> factorize(22)
    [2, 11]
    >>> factorize(23)
    [23]
    >>> factorize(24)
    [2, 2, 2, 3]
    >>> factorize(25)
    [5, 5]
    >>> factorize(26)
    [2, 13]
    >>> factorize(27)
    [3, 3, 3]
    >>> factorize(28)
    [2, 2, 7]
    >>> factorize(29)
    [29]
    >>> factorize(30)
    [2, 3, 5]
    >>> factorize(31)
    [31]
    >>> factorize(32)
    [2, 2, 2, 2, 2]
    >>> factorize(33)
    [3, 11]
    >>> factorize(34)
    [2, 17]
    >>> factorize(35)
    [5, 7]
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
