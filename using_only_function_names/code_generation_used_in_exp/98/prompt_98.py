
def count_upper(s):
    """
    Counts the number of upper case letters in a string.
    """
    return sum(1 for c in s if c.isupper())
