

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
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join([c for c in text if c not in vowels])
