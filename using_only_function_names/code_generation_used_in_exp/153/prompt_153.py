
def Strongest_Extension(class_name, extensions):
    """
    Checks if the file name is valid.
    :param file_name: file name to check.
    :return: True if the file name is valid, False otherwise.
    """
    if len(class_name) == 0:
        return False
    last_char = class_name[-1]
    if last_char.isalpha():
        return True
    else:
        return False
