from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    """
    result = []
    current_level = 0
    max_level = 0
    for ch in paren_string:
        if ch == ' ':
            if max_level > 0:
                result.append(max_level)
                current_level = 0
                max_level = 0
        elif ch == '(':
            current_level += 1
            max_level = max(max_level, current_level)
        elif ch == ')':
            current_level -= 1
    if max_level > 0:
        result.append(max_level)
    return result
