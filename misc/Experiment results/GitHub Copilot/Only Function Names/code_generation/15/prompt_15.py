

def string_sequence(n: int) -> str:
    """Return a string of length n consisting of the numbers 1 through n
    separated by spaces.
    
    >>> string_sequence(1)
    '1'
    >>> string_sequence(2)
    '1 2'
    >>> string_sequence(3)
    '1 2 3'
    >>> string_sequence(4)
    '1 2 3 4'
    >>> string_sequence(5)
    '1 2 3 4 5'
    """
    result = ""
    for i in range(1, n + 1):
        result += str(i) + " "
    return result[:-1]