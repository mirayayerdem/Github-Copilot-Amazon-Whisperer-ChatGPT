

def strlen(string: str) -> int:
    """Return the length of the string.
    
    >>> strlen("hello")
    5
    >>> strlen("hello world")
    11
    >>> strlen("")
    0
    """
    length = 0
    for char in string:
        length += 1
    return length
