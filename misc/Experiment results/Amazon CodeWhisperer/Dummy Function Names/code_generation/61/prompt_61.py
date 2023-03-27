

def foo(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> foo("(")
    False
    >>> foo("()")
    True
    >>> foo("(()())")
    True
    >>> foo(")(()")
    False
    """
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return not stack
