
def int_to_mini_roman(number):
    """
    Returns the Roman numeral of number.
    :param number: Integer.
    :return: The Roman numeral of number.
    """
    roman_numeral = ""
    roman_numeral += "M" * (number // 1000)
    number = number % 1000
    roman_numeral += "D" * (number // 500)
    number = number % 500
    roman_numeral += "C" * (number // 100)
    number = number % 100
    roman_numeral += "L" * (number // 50)
    number = number % 50
    roman_numeral += "X" * (number // 10)
    number = number % 10
    roman_numeral += "V" * (number // 5)
    number = number % 5
    roman_numeral += "I" * number
    return roman_numeral

    

