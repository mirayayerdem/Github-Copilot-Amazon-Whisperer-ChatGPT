from typing import List


def all_prefixes(string: str) -> List[str]:
    """Return a list of all prefixes of the string.
    
    >>> all_prefixes("hello")
    ['h', 'he', 'hel', 'hell', 'hello']
    >>> all_prefixes("world")
    ['w', 'wo', 'wor', 'worl', 'world']
    >>> all_prefixes("hello world")
    ['h', 'he', 'hel', 'hell', 'hello', 'hello ', 'hello w', 'hello wo', 'hello wor', 'hello worl', 'hello world']
    >>> all_prefixes("")
    []
    """
    result = []
    for i in range(len(string)):
        result.append(string[:i+1])
    return result