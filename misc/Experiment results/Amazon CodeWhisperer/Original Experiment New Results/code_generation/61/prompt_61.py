

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # "stack" is a list of indices of open brackets
    stack = []
    for i, bracket in enumerate(brackets):
        if bracket == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack
