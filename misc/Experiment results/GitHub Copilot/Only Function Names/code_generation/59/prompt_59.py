

def largest_prime_factor(n: int):
    """Return the largest prime factor of n.
    >>> largest_prime_factor(1)
    1
    >>> largest_prime_factor(2)
    2
    >>> largest_prime_factor(3)
    3
    >>> largest_prime_factor(4)
    2
    >>> largest_prime_factor(5)
    5
    >>> largest_prime_factor(6)
    3
    >>> largest_prime_factor(7)
    7
    >>> largest_prime_factor(8)
    2
    >>> largest_prime_factor(9)
    3
    >>> largest_prime_factor(10)
    5
    >>> largest_prime_factor(11)
    11
    >>> largest_prime_factor(12)
    3
    >>> largest_prime_factor(13)
    13
    >>> largest_prime_factor(14)
    7
    >>> largest_prime_factor(15)
    5
    >>> largest_prime_factor(16)
    2
    >>> largest_prime_factor(17)
    17
    >>> largest_prime_factor(18)
    3
    >>> largest_prime_factor(19)
    19
    >>> largest_prime_factor(20)
    5
    >>> largest_prime_factor(21)
    7
    >>> largest_prime_factor(22)
    11
    >>> largest_prime_factor(23)
    23
    >>> largest_prime_factor(24)
    3
    >>> largest_prime_factor(25)
    5
    >>> largest_prime_factor(26)
    13
    >>> largest_prime_factor(27)
    3
    >>> largest_prime_factor(28)
    7
    >>> largest_prime_factor(29)
    29
    >>> largest_prime_factor(30)
    5
    >>> largest_prime_factor(31)
    31
    >>> largest_prime_factor(32)
    2
    >>> largest_prime_factor(33)
    11
    >>> largest_prime_factor(34)
    17
    >>> largest_prime_factor(35)
    7
    >>> largest_prime_factor(36)
    3
    >>> largest_prime_factor(37)
    37
    >>> largest_prime_factor(38)
    19
    >>> largest_prime_factor(39)
    13
    >>> largest_prime_factor(40)
    5
    >>> largest_prime_factor(41)
    """
    "*** YOUR CODE HERE ***"
    if is_prime(n):
        return n
    else:
        for i in range(2, n):
            if n % i == 0:
                return largest_prime_factor(n // i)

def is_prime(n: int) -> bool:
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
    
