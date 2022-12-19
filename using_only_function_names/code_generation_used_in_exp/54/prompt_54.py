

def same_chars(s0: str, s1: str):
    """
    Checks if two strings have the same characters.
    :param s0: First string.
    :param s1: Second string.
    :return: True if the strings have the same characters, False otherwise.
    """
    return set(s0) == set(s1)
