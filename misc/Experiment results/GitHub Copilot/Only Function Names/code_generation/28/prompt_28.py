from typing import List


def concatenate(strings: List[str]) -> str:
    """Return a string consisting of the concatenation of the strings in the list.
    
    >>> concatenate(["hello", "world"])
    'helloworld'
    >>> concatenate(["hello", "world", "hello world"])
    'helloworldhello world'
    >>> concatenate(["hello", "world", "hello world", "hello world!"])
    'helloworldhello worldhello world!'
    >>> concatenate([])
    ''
    """
    result = ""
    for string in strings:
        result += string
    return result
