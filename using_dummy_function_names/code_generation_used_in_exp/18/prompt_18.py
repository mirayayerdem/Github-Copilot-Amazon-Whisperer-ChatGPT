

def foo(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> foo('', 'a')
    0
    >>> foo('aaa', 'a')
    3
    >>> foo('aaaa', 'aa')
    3
    """
    return string.count(substring)
