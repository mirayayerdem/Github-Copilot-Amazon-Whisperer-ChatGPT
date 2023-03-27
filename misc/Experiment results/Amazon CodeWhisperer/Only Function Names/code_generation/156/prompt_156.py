
def int_to_mini_roman(number):
    """
    Converts an integer to a mini-roman number.
    """
    roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                  5: 'V', 4: 'IV', 1: 'I'}
    roman_number = ''
    for key in roman_dict:
        while number >= key:
            roman_number += roman_dict[key]
            number -= key
    return roman_number

    

