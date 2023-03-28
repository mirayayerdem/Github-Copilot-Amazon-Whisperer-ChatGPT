
def is_nested(string):
    """ (str) -> bool

    Return True if and only if string has one or more pairs of matching
    parentheses.

    >>> is_nested('(())')
    True
    >>> is_nested('((())')
    False
    >>> is_nested('()')
    True
    >>> is_nested('')
    False
    >>> is_nested('a(b)c')
    False
    """
    # The number of open parentheses seen so far.
    open_parens = 0

    for char in string:
        if char == '(':
            open_parens = open_parens + 1
        elif char == ')':
            open_parens = open_parens - 1

    return open_parens == 0