def do_algebra(operator, operand):
    if operator == '+':
        return operand[0] + operand[1]
    elif operator == '-':
        return operand[0] - operand[1]
    elif operator == '*':
        return operand[0] * operand[1]
    elif operator == '/':
        return operand[0] / operand[1]
    else:
        return "Invalid operator"
