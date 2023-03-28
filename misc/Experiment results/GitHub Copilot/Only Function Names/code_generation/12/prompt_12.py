from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """Return the longest string in the list.
    
    >>> longest(["hello", "world"])
    'world'
    >>> longest(["hello", "world", "hello world"])
    'hello world'
    >>> longest(["hello", "world", "hello world", "hello world!"])
    'hello world!'
    >>> longest(["hello", "world", "hello world", "hello world!", ""])
    'hello world!'
    >>> longest([])
    """
    if len(strings) == 0:
        return None
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string