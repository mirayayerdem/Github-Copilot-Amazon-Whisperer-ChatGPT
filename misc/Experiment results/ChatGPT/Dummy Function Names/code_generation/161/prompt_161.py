
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
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    is_contains_letter = False
    for ch in s:
        if ch in letters:
            is_contains_letter = True
            if ch.islower():
                result += ch.upper()
            else:
                result += ch.lower()
        else:
            result += ch
    if not is_contains_letter:
        result = result[::-1]
    return result
