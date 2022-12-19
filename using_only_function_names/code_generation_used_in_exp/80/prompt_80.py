
def is_happy(s):
    """
    Return True if the given string is a happy string.

    A happy string is a string that:
    - consists only of letters in the set ['a', 'b', 'c']
    - has no adjacent characters that are the same
    - does not contain the string 'aaa'
    """
    if len(s) == 0:
        return False
    if len(s) == 1:
        return s in ['a', 'b', 'c']
    if s[0] == s[1] or s[0] == s[-1] or s[-1] == s[-2]:
        return False
    if s[0] == s[-1]:
        return is_happy(s[1:-1])
    if s[1] == s[-1]:
        return is_happy(s[2:-2])
    if s[2] == s[-2]:
        return is_happy(s[3:-3])
    return is_happy(s[1:-1])