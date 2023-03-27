from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    curr_count = 0
    for char in paren_string:
        if char == '(':
            curr_count += 1
        elif char == ')':
            result.append(curr_count)
            curr_count -= 1
    return result

