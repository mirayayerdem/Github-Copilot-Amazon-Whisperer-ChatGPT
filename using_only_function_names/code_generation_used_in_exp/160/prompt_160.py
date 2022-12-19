
def do_algebra(operator, operand):
    if operator == '+':
        return operand
    elif operator == '-':
        return -operand
    elif operator == '*':
        return operand * operand
    elif operator == '/':
        return operand / operand
    elif operator == '**':
        return operand ** operand
    elif operator == '%':
        return operand % operand
    else:
        raise ValueError('Unknown operator: ' + operator)




