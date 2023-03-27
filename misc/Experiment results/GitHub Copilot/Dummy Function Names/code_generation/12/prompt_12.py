from typing import List, Optional


def foo(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> foo([])

    >>> foo(['a', 'b', 'c'])
    'a'
    >>> foo(['a', 'bb', 'ccc'])
    'ccc'
    """
    if len(strings) == 0:
        return None
    result = strings[0]
    for string in strings:
        if len(string) > len(result):
            result = string
    return result
