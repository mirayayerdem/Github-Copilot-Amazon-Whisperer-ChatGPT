
def check_if_last_char_is_a_letter(txt):
    """
    Checks if the last character of a string is a letter.
    :param txt: string to check.
    :return: True if the last character is a letter, False otherwise.
    """
    if len(txt) == 0:
        return False
    last_char = txt[-1]
    if last_char.isalpha():
        return True
    else:
        return False

