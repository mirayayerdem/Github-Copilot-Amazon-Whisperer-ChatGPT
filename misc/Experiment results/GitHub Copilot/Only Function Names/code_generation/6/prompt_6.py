from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """Return a list of integers corresponding to the number of nested
    parentheses in the string.

    >>> parse_nested_parens("()")
    [1, 1]
    >>> parse_nested_parens("(()())")
    [1, 2, 2, 1, 1, 1]
    >>> parse_nested_parens("(((())))")
    [1, 2, 3, 3, 3, 2, 1]
    >>> parse_nested_parens("(((())))()")
    [1, 2, 3, 3, 3, 2, 1, 1, 1]
    >>> parse_nested_parens("(((())))()()")
    [1, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1]
    """
    result = []
    depth = 0
    for char in paren_string:
        if char == "(":
            depth += 1
            result.append(depth)
        elif char == ")":
            result.append(depth)
            depth -= 1
    return result