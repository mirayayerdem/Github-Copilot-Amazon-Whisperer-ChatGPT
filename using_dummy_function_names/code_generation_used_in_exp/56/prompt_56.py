

def foo(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> foo("<")
    False
    >>> foo("<>")
    True
    >>> foo("<<><>>")
    True
    >>> foo("><<>")
    False
    """
    stack = []
    for ch in brackets:
        if ch == "<":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
