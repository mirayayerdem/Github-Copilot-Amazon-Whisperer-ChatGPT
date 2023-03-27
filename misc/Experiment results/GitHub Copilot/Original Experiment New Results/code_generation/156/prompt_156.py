
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # roman numerals
    roman = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }
    # get the largest roman numeral that is less than or equal to the number
    largest = max([i for i in roman.keys() if i <= number])
    # subtract the largest roman numeral from the number
    number -= largest
    # if the number is 0, return the roman numeral
    if number == 0:
        return roman[largest]
    # otherwise, return the roman numeral and the roman numeral of the remaining number
    return roman[largest] + int_to_mini_roman(number)
    
