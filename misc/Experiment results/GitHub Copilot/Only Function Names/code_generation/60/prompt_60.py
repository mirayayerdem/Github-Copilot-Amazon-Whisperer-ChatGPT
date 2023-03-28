

def sum_to_n(n: int):
    """Return the sum of all numbers from 1 to n.
    >>> sum_to_n(1)
    1
    >>> sum_to_n(2)
    3
    >>> sum_to_n(3)
    6
    >>> sum_to_n(4)
    10
    >>> sum_to_n(5)
    15
    >>> sum_to_n(6)
    21
    >>> sum_to_n(7)
    28
    >>> sum_to_n(8)
    36
    >>> sum_to_n(9)
    45
    >>> sum_to_n(10)
    55
    """
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)
