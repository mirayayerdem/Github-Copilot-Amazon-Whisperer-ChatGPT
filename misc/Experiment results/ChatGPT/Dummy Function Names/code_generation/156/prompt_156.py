
def foo(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> foo(19) == 'xix'
    >>> foo(152) == 'clii'
    >>> foo(426) == 'cdxxvi'
    """
    roman = ""
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    for i, val in enumerate(values):
        while number >= val:
            roman += numerals[i]
            number -= val
    return roman.lower()
