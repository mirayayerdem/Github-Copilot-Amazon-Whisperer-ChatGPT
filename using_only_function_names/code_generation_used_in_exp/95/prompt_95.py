
def check_dict_case(dict):
    """
    Checks if a dictionary has all keys in lowercase.
    :param dict: dictionary to check.
    :return: True if all keys in dict are lowercase, False otherwise.
    """
    for key in dict:
        if key.isupper():
            return False
    return True
