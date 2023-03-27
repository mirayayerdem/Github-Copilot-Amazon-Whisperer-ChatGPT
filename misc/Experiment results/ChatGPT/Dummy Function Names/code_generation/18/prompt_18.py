def foo(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> foo('', 'a')
    0
    >>> foo('aaa', 'a')
    3
    >>> foo('aaaa', 'aa')
    3
    """
    count = 0
    start = 0
    while start < len(string):
        start = string.find(substring, start) + 1
        if start > 0:
            count += 1
    return count
