
def foo(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    foo("1234") = "4321"
    foo("ab") = "AB"
    foo("#a@C") = "#A@c"
    """
    return "".join(c.lower() if c.isalpha() else c.upper() if c.isupper() else c for c in s)
