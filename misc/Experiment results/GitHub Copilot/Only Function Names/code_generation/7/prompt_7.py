from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Return a list of strings that contain the substring.
    
    >>> filter_by_substring(["hello", "world", "hello world"], "hello")
    ['hello', 'hello world']
    >>> filter_by_substring(["hello", "world", "hello world"], "world")
    ['world', 'hello world']
    >>> filter_by_substring(["hello", "world", "hello world"], "o")
    ['hello', 'world', 'hello world']
    >>> filter_by_substring(["hello", "world", "hello world"], "x")
    []
    """
    result = []
    for string in strings:
        if substring in string:
            result.append(string)
    return result
