from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Return a list of strings that start with the prefix.
    
    >>> filter_by_prefix(["hello", "world", "hello world"], "hello")
    ['hello', 'hello world']
    >>> filter_by_prefix(["hello", "world", "hello world"], "world")
    ['world']
    >>> filter_by_prefix(["hello", "world", "hello world"], "o")
    []
    >>> filter_by_prefix(["hello", "world", "hello world"], "x")
    []
    """
    result = []
    for string in strings:
        if string.startswith(prefix):
            result.append(string)
    return result
