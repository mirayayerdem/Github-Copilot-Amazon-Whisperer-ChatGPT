

def modp(n: int, p: int):
    """Return the remainder of n divided by p.
    >>> modp(5, 2)
    1
    >>> modp(5, 3)
    2
    >>> modp(5, 4)
    1
    >>> modp(5, 5)
    0
    >>> modp(5, 6)
    5
    >>> modp(5, 7)
    5
    >>> modp(5, 8)
    5
    >>> modp(5, 9)
    5
    >>> modp(5, 10)
    5
    >>> modp(5, 11)
    5
    >>> modp(5, 12)
    5
    >>> modp(5, 13)
    5
    >>> modp(5, 14)
    5
    >>> modp(5, 15)
    5
    >>> modp(5, 16)
    5
    >>> modp(5, 17)
    5
    >>> modp(5, 18)
    5
    >>> modp(5, 19)
    5
    >>> modp(5, 20)
    5
    >>> modp(5, 21)
    5
    >>> modp(5, 22)
    5
    >>> modp(5, 23)
    5
    >>> modp(5, 24)
    5
    >>> modp(5, 25)
    5
    >>> modp(5, 26)
    5
    >>> modp(5, 27)
    5
    >>> modp(5, 28)
    5
    >>> modp(5, 29)
    5
    >>> modp(5, 30)
    5
    >>> modp(5, 31)
    5
    >>> modp(5, 32)
    5
    >>> modp(5, 33)
    5
    >>> modp(5, 34)
    5
    >>> modp(5, 35)
    5
    >>> modp(5, 36)
    """
    "*** YOUR CODE HERE ***"
    if n < p:
        return n
    else:
        return modp(n - p, p)
