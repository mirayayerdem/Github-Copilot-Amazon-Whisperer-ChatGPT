

def foo(text: str):
    """
    Checks if given string is a palindrome
    >>> foo('')
    True
    >>> foo('aba')
    True
    >>> foo('aaaaa')
    True
    >>> foo('zbcd')
    False
    """
    return text == text[::-1]
