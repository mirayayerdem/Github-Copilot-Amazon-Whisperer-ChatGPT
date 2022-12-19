

def flip_case(string: str) -> str:
    """
    Flips the case of all characters in a string.
    :param string: String to flip case of.
    :return: String with flipped case.
    """
    flipped_string = ""
    for c in string:
        if c.isupper():
            flipped_string += c.lower()
        else:
            flipped_string += c.upper()
    return flipped_string
