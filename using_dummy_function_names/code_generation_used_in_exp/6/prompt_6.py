from typing import List


def foo(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> foo('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_list = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            paren_list.append(0)
            i += 1
        elif paren_string[i] == ')':
            paren_list[-1] += 1
            paren_list.pop()
            i += 1
        else:
            i += 1
    return paren_list
