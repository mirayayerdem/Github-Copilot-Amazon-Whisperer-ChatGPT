

def is_prime(n):
    """Return whether n is prime.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    >>> is_prime(14)
    False
    >>> is_prime(15)
    False
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(19)
    True
    >>> is_prime(20)
    False
    >>> is_prime(21)
    False
    >>> is_prime(22)
    False
    >>> is_prime(23)
    True
    >>> is_prime(24)
    False
    >>> is_prime(25)
    False
    >>> is_prime(26)
    False
    >>> is_prime(27)
    False
    >>> is_prime(28)
    False
    >>> is_prime(29)
    True
    >>> is_prime(30)
    False
    >>> is_prime(31)
    True
    >>> is_prime(32)
    False
    >>> is_prime(33)
    False
    >>> is_prime(34)
    False
    >>> is_prime(35)
    False
    >>> is_prime(36)
    False
    >>> is_prime(37)
    True
    >>> is_prime(38)
    False
    >>> is_prime(39)
    False
    >>> is_prime(40)
    False
    >>> is_prime(41)
    True
    >>> is_prime(42)
    False
    >>> is_prime(43)
    True
    >>> is_prime(44)
    False
    >>> is_prime(45)
    False
    >>> is_prime(46)
    False
    >>> is_prime(47)
    True
    >>> is_prime(48)
    False
    >>> is_prime(49)
    False
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
