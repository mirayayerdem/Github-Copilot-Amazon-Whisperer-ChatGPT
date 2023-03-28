
def int_to_mini_roman(number):
    """Converts a number from 1 to 10 to a mini-roman numeral."""
    if number == 1:
        return "i"
    elif number == 2:
        return "ii"
    elif number == 3:
        return "iii"
    elif number == 4:
        return "iv"
    elif number == 5:
        return "v"
    elif number == 6:
        return "vi"
    elif number == 7:
        return "vii"
    elif number == 8:
        return "viii"
    elif number == 9:
        return "ix"
    elif number == 10:
        return "x"
    else:
        return "Number out of range."