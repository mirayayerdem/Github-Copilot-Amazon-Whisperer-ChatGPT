from typing import List


def foo(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> foo('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    for c in paren_string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
        elif c == ' ':
            continue
        else:
            raise Exception("Invalid character in input string")
        if len(stack) == 0:
            result.append(paren_string[:paren_string.find(c) + 1])
            paren_string = paren_string[paren_string.find(c) + 1:]
    return result




