
def file_name_check(file_name):
    """
    Checks if the file name is valid.
    :param file_name: file name to check.
    :return: True if the file name is valid, False otherwise.
    """
    if len(file_name) == 0:
        return False
    last_char = file_name[-1]
    if last_char.isalpha():
        return True
    else:
        return False
