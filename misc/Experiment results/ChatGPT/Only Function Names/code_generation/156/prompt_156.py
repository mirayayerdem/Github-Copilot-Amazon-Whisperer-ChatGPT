def int_to_mini_roman(number):
    roman = ""
    while number >= 1000:
        roman += "M"
        number -= 1000
    while number >= 500:
        roman += "D"
        number -= 500
    while number >= 100:
        roman += "C"
        number -= 100
    while number >= 50:
        roman += "L"
        number -= 50
    while number >= 10:
        roman += "X"
        number -= 10
    while number >= 5:
        roman += "V"
        number -= 5
    while number >= 1:
        roman += "I"
        number -= 1
    return roman
