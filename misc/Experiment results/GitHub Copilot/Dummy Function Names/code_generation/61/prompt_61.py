

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
    return brackets.count("(") == brackets.count(")")
