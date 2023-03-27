from typing import List

def foo(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> foo('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    max_nesting = []
    for group in groups:
        current_nesting = 0
        max_current = 0
        for char in group:
            if char == "(":
                current_nesting += 1
                max_current = max(max_current, current_nesting)
            elif char == ")":
                current_nesting -= 1
        max_nesting.append(max_current)
    return max_nesting
