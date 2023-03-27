
def is_nested(string):
    '''
    This function takes a string as an input and returns True if the string is nested, False otherwise.
    '''
    if string == '':
        return False
    if string[0] == '(' and string[-1] == ')':
        return is_nested(string[1:-1])
    else:
        return False

