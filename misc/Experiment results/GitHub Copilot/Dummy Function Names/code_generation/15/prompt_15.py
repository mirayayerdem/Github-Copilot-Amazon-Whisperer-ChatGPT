

def foo(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> foo(0)
    '0'
    >>> foo(5)
    '0 1 2 3 4 5'
    """
    result = []
    for i in range(n + 1):
        result.append(str(i))
    return ' '.join(result)
