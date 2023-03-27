
def match_parens(lst):
    stack = []
    for s in lst:
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack:
                    return False
                else:
                    stack.pop()
    return not stack
