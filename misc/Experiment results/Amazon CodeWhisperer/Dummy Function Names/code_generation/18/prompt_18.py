

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
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
