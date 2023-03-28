

def largest_divisor(n: int) -> int:

    """Return the largest divisor of n that is less than n.

    >>> largest_divisor(1)
    1
    >>> largest_divisor(2)
    1
    >>> largest_divisor(3)
    1
    >>> largest_divisor(4)
    2
    >>> largest_divisor(5)
    1
    >>> largest_divisor(6)
    3
    >>> largest_divisor(7)
    1
    >>> largest_divisor(8)
    4
    >>> largest_divisor(9)
    3
    >>> largest_divisor(10)
    5
    >>> largest_divisor(11)
    1
    >>> largest_divisor(12)
    6
    >>> largest_divisor(13)
    1
    >>> largest_divisor(14)
    7
    >>> largest_divisor(15)
    5
    >>> largest_divisor(16)
    8
    >>> largest_divisor(17)
    1
    >>> largest_divisor(18)
    9
    >>> largest_divisor(19)
    1
    >>> largest_divisor(20)
    10
    """

    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1

    return 1