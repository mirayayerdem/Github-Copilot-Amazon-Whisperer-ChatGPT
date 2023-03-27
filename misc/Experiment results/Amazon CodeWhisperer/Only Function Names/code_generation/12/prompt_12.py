from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    >>> longest(['a', 'ab', 'abc'])
    'abc'
    >>> longest(['abc', 'ab', 'a'])
    'abc'
    >>> longest(['abc', 'ab', 'abcd'])
    'abcd'
    >>> longest(['abc', 'abcd', 'ab'])
    'abcd'
    >>> longest(['abc', 'abcd', 'abcde'])
    'abcde'
    >>> longest(['abc', 'abcd', 'abcde', 'ab'])
    'abcde'
    >>> longest(['abc', 'abcd', 'abcde', 'ab', 'abc'])
    'abcde'
    >>> longest(['abc', 'abcd', 'abcde', 'ab', 'abc', 'abcd'])
    'abcde'
    >>> longest(['abc', 'abcd', 'abcde', 'ab', 'abc', 'abcd', 'abcde'])
    'abcde'

