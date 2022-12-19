

def foo(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> foo('xyzXYZ')
    3
    >>> foo('Jerry')
    4
    """
    return len(set(string.lower()))
