

def change_base(x: int, base: int):
    """Return the base-10 representation of x in base base.
    
    >>> change_base(100, 2)
    4
    >>> change_base(100, 3)
    10
    >>> change_base(100, 4)
    20
    >>> change_base(100, 5)
    40
    >>> change_base(100, 6)
    22
    >>> change_base(100, 7)
    14
    >>> change_base(100, 8)
    4
    >>> change_base(100, 9)
    11
    >>> change_base(100, 10)
    100
    >>> change_base(100, 11)
    91
    >>> change_base(100, 12)
    82
    >>> change_base(100, 13)
    73
    >>> change_base(100, 14)
    64
    >>> change_base(100, 15)
    55
    >>> change_base(100, 16)
    46
    >>> change_base(100, 17)
    37
    >>> change_base(100, 18)
    28
    >>> change_base(100, 19)
    19
    >>> change_base(100, 20)
    10
    >>> change_base(100, 21)
    1
    """
    if x == 0:
        return 0
    else:
        return x % base + 10 * change_base(x // base, base)
