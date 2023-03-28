
def match_parens(lst):
    """ (list of str) -> bool

    Return True if every opening parenthesis in lst has a matching closing
    parenthesis after it and False otherwise.

    >>> match_parens(['(', 'x', '+', 'y', ')'])
    True
    >>> match_parens(['(', 'x', '+', 'y'])
    False
    """
    count = 0
    for i in lst:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    return count == 0