from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separates parentheses groups from a string.
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
