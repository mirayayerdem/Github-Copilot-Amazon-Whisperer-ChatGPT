

def foo(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> foo(8, 3)
    '22'
    >>> foo(8, 2)
    '1000'
    >>> foo(7, 2)
    '111'
    """
    res = ""
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res

