

def correct_bracketing(brackets: str):
    """
    Checks if the brackets in a string are correctly nested.
    :param brackets: String with brackets.
    :return: True if the brackets are correctly nested, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket in ['(', '[', '{']:
            stack.append(bracket)
        elif bracket in [')', ']', '}']:
            if len(stack) == 0:
                return False
            if bracket == ')' and stack[-1] != '(':
                return False
            if bracket == ']' and stack[-1] != '[':
                return False
            if bracket == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return len(stack) == 0

