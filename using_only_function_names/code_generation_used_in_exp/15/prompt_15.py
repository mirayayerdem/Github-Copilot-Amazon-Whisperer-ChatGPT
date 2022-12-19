

def string_sequence(n: int) -> str:
    """
    Generate a string of n length containing the numbers 0 to n-1.
    :param n: Length of the string.
    :return: String of length n containing the numbers 0 to n-1.
    """
    return ''.join(str(i) for i in range(n))
