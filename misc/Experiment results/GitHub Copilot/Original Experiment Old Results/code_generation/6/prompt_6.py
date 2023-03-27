from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_groups = separate_paren_groups(paren_string)
    return [max(map(count_parens, group)) for group in paren_groups]


def count_parens(paren_string: str) -> int:
    """ Count the number of open and closed parentheses in a string.
    >>> count_parens('(()()) ((())) () ((())()())')
    8
    """
    open_count = 0
    closed_count = 0
    for char in paren_string:
        if char == '(':
            open_count += 1
        elif char == ')':
            closed_count += 1
    return open_count + closed_count


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []
    paren_stack = []
    for char in paren_string:
        if char == '(':
            paren_stack.append(char)
        elif char == ')':
            if len(paren_stack) == 0:
                paren_groups.append(''.join(paren_stack))
                paren_stack = []
            else:
                paren_stack.pop()
    return paren_groups

    





