

def correct_bracketing(brackets: str):
    """Return True if brackets is correctly bracketed, False otherwise.
    >>> correct_bracketing('((()))')
    True
    >>> correct_bracketing('(()')
    False
    >>> correct_bracketing('())')
    False
    >>> correct_bracketing('((())')
    False
    >>> correct_bracketing('(()(()))')
    True
    >>> correct_bracketing('(()()(()))')
    True
    >>> correct_bracketing('(()()(()))()')
    True
    >>> correct_bracketing('(()()(()))())')
    False
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            count += 1
        elif brackets[i] == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
