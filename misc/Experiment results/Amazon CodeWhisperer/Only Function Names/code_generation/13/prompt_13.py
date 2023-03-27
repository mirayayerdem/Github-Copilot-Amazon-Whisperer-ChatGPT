

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of two integers.
    """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)