

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
    for bracket in brackets:
    	if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0 or stack.pop() != "<":
                return False
    return len(stack) == 0