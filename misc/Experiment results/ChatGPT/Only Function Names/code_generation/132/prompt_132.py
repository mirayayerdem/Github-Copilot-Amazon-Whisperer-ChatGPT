def is_nested(string):
    stack = []
    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')' or char == '}' or char == ']':
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == '}' and stack[-1] != '{':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return not stack
