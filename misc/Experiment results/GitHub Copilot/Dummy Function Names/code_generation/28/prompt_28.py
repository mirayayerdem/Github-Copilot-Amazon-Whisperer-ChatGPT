from typing import List


def foo(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> foo([])
    ''
    >>> foo(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
