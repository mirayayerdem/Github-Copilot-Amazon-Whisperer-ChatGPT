from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    groups = []
    current_group = []
    balance = 0
    for ch in paren_string:
        if ch == ' ':
            continue
        elif ch == '(':
            balance += 1
            current_group.append(ch)
        elif ch == ')':
            balance -= 1
            current_group.append(ch)
            if balance == 0:
                groups.append(''.join(current_group))
                current_group = []
    return groups
