from typing import List

def foo(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> foo([])
    ''
    >>> foo(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)

