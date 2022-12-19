from typing import List


def foo(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> foo('010', '110')
    '100'
    """
    return ''.join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))
