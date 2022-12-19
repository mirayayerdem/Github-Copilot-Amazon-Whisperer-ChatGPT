from typing import List


def string_xor(a: str, b: str) -> str:
    """
    XOR two strings together.
    :param a: First string.
    :param b: Second string.
    :return: XOR of the two strings.
    """
    if len(a) != len(b):
        raise ValueError('Strings must be the same length.')
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result
