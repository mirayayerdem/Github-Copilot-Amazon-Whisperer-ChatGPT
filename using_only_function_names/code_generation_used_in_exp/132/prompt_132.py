
def is_nested(string):
    """
    Return True if string is a nested string.
    """
    if len(string) == 0:
        return False
    if len(string) == 1:
        return False
    if string[0] == '"' and string[-1] == '"':
        return True
    if string[0] == "'" and string[-1] == "'":
        return True
    return is_nested(string[1:])

