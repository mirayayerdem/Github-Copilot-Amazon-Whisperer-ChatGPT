from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    curr_group = ""
    in_group = False
    for char in paren_string:
        if char == '(':
            in_group = True
        elif char == ')':
            in_group = False
            result.append(curr_group)
            curr_group = ""
        elif in_group:
            curr_group += char
    return result
