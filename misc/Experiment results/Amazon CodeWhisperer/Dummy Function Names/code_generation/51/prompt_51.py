

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
    vowels = 'aeiouAEIOU'
    for i in text:
        if i in vowels:
            text = text.replace(i, "")
    return text
