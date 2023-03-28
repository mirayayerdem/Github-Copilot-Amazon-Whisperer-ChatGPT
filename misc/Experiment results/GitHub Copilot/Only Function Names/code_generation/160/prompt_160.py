
def do_algebra(operator, operand):
    if operator == "add":
        return operand + 1
    elif operator == "subtract":
        return operand - 1
    elif operator == "multiply":
        return operand * 2
    elif operator == "divide":
        return operand / 2
    else:
        return "Invalid operator"