

def foo(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> foo('Hello')
    'hELLO'
    """
    return ''.join([chr(ord(c) ^ (1 << 5)) for c in string])
