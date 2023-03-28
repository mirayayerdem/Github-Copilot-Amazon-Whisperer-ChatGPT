
def anti_shuffle(s):
    """Return a string with the characters in s in reverse order."""
    result = ''
    for c in s:
        result = c + result
    return result