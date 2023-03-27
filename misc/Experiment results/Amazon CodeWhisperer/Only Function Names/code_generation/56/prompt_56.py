

def correct_bracketing(brackets: str):
    """
    Returns True if brackets are correctly bracketed, else False.
    """
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
