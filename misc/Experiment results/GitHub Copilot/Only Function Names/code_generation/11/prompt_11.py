from typing import List


def string_xor(a: str, b: str) -> str:
    """Return the xor of two strings.
    
    >>> string_xor("hello", "world")
    'wello'
    >>> string_xor("hello", "hello")
    'hello'
    >>> string_xor("hello", "world!")
    'wello!'
    >>> string_xor("hello", "world!!")
    'wello!!'
    """
    result = ""
    for i in range(min(len(a), len(b))):
        result += chr(ord(a[i]) ^ ord(b[i]))
    return result