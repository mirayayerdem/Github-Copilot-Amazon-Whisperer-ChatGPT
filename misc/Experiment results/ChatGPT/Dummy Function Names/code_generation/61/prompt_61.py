

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
    for char in brackets:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
