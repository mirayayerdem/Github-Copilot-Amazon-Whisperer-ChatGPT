from typing import List


def foo(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> foo('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_list = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            paren_list.append('')
            i += 1
        elif paren_string[i] == ')':
            paren_list[-1] += paren_string[i]
            paren_list.pop()
            i += 1
        else:
            paren_list[-1] += paren_string[i]
            i += 1
    return paren_list