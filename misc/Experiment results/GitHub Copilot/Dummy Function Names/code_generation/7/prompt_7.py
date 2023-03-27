from typing import List


def foo(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> foo([], 'a')
    []
    >>> foo(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    result = []
    for string in strings:
        if substring in string:
            result.append(string)
    return result
