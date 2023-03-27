

def foo(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> foo('')
    ''
    >>> foo("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> foo('abcdef')
    'bcdf'
    >>> foo('aaaaa')
    ''
    >>> foo('aaBAA')
    'B'
    >>> foo('zbcd')
    'zbcd'
    """
    return "".join([ch for ch in text if ch not in "aeiouAEIOU"])
