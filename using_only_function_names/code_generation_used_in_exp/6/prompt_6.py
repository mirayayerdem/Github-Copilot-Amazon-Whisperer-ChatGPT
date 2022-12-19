from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parses a string containing parentheses.
    :param paren_string: String containing parentheses.
    :return: List of parentheses groups.
    """
    paren_groups = []
    paren_group = ''
    for c in paren_string:
        if c == '(':
            paren_group += c
        elif c == ')':
            paren_group += c
            paren_groups.append(paren_group)
            paren_group = ''
        else:
            paren_group += c
    return paren_groups

