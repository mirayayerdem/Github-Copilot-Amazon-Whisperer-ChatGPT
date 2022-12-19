

def correct_bracketing(brackets: str):
    """
    Checks if a string of brackets is correctly bracketed.
    :param brackets: String of brackets.
    :return: True if the string is correctly bracketed, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == '(' or bracket == '{' or bracket == '[':
            stack.append(bracket)
        elif bracket == ')' and stack[-1] == '(':
            stack.pop()
        elif bracket == '}' and stack[-1] == '{':
            stack.pop()
        elif bracket == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return len(stack) == 0

