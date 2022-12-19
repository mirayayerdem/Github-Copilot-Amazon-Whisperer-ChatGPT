
def reverse_delete(s,c):
    """
    Return a string that is the reverse of s with all characters
    that are in c removed.
    """
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s if s not in c else ''
    if s[0] in c:
        return reverse_delete(s[1:],c)
    return s[0] + reverse_delete(s[1:],c)
