from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Given a string of parentheses, return a list of the
    corresponding opening and closing paren indices.
    """
    open_parens = []
    close_parens = []
    for i, char in enumerate(paren_string):
        if char == "(":
            open_parens.append(i)
        elif char == ")":
            close_parens.append(i)
    return [open_parens, close_parens]

