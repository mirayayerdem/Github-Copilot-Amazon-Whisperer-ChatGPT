from typing import List

def foo(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> foo('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]
