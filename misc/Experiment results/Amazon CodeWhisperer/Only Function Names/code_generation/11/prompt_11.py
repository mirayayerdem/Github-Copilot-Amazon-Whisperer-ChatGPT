from typing import List


def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of equal length
    """
    assert len(a) == len(b)
    return "".join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))
