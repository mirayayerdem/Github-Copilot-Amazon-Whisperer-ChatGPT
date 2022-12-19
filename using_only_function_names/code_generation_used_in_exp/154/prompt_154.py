
def cycpattern_check(a , b):
    """
    Checks if the file name is valid.
    :param file_name: file name to check.
    :return: True if the file name is valid, False otherwise.
    """
    if len(a) == 0:
        return False
    last_char = a[-1]
    if last_char.isalpha():
        return True
    else:
        return False

