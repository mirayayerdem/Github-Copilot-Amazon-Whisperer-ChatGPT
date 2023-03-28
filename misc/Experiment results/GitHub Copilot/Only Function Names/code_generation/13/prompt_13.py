

def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b.
    
    >>> greatest_common_divisor(10, 15)
    5
    >>> greatest_common_divisor(10, 20)
    10
    >>> greatest_common_divisor(10, 25)
    5
    >>> greatest_common_divisor(10, 30)
    10
    >>> greatest_common_divisor(10, 35)
    5
    >>> greatest_common_divisor(10, 40)
    10
    >>> greatest_common_divisor(10, 45)
    5
    >>> greatest_common_divisor(10, 50)
    10
    >>> greatest_common_divisor(10, 55)
    5
    >>> greatest_common_divisor(10, 60)
    10
    >>> greatest_common_divisor(10, 65)
    5
    >>> greatest_common_divisor(10, 70)
    10
    >>> greatest_common_divisor(10, 75)
    5
    >>> greatest_common_divisor(10, 80)
    10
    >>> greatest_common_divisor(10, 85)
    5
    >>> greatest_common_divisor(10, 90)
    10
    >>> greatest_common_divisor(10, 95)
    5
    >>> greatest_common_divisor(10, 100)
    10
    >>> greatest_common_divisor(10, 105)
    5
    >>> greatest_common_divisor(10, 110)
    10
    >>> greatest_common_divisor(10, 115)
    5
    >>> greatest_common_divisor(10, 120)
    10
    >>> greatest_common_divisor(10, 125)
    5
    >>> greatest_common_divisor(10, 130)
    10
    >>> greatest_common_divisor(10, 135)
    5
    >>> greatest_common_divisor(10, 140)
    10
    >>> greatest_common_divisor(10, 145)
    5
    >>> greatest_common_divisor(10, 150)
    10
    >>> greatest_common_divisor(10, 155)
    5
    >>> greatest_common_divisor(10, 160)
    10
    >>> greatest_common_divisor
    """
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return greatest_common_divisor(a % b, b)
    return greatest_common_divisor(a, b % a)