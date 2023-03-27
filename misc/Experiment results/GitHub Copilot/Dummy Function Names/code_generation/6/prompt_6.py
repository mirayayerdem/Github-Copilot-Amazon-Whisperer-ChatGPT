from typing import List


def foo(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> foo('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    stack = []
    for c in paren_string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
        elif c == ' ':
            result.append(len(stack))
            stack = []
        else:
            raise Exception("Invalid character in input string")
    return result
