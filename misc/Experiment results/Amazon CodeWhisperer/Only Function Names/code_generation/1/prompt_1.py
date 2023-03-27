from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Given a string of parentheses, return a list of all the separate groups of
    parentheses.
    """
    result = []
    current_group = []
    for char in paren_string:
        if char == "(":
            current_group.append(char)
        elif char == ")":
            current_group.append(char)
            result.append("".join(current_group))
            current_group = []
        else:
            raise ValueError(f"Invalid character {char}")
    return result
