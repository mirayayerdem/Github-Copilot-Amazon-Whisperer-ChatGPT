from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    >>> all_prefixes("abc")
    ['a', 'ab', 'abc']
    >>> all_prefixes("a")
    ['a']
    """
    return [string[:i] for i in range(len(string) + 1)]
