

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor of two numbers.
    :param a: First number.
    :param b: Second number.
    :return: Greatest common divisor.
    """
    while b != 0:
        a, b = b, a % b
    return a
