from typing import List


def foo(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> foo([], 'a')
    []
    >>> foo(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    result = []
    for string in strings:
        if string.startswith(prefix):
            result.append(string)
    return result
