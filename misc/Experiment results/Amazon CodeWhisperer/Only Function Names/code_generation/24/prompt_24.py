

def largest_divisor(n: int) -> int:
    """
    Returns the largest divisor of n.
    """
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor
