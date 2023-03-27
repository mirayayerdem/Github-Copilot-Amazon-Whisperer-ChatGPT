

def count_distinct_characters(string: str) -> int:
    """
    Counts the number of distinct characters in a string.
    :param string: The string to count the characters of.
    :return: The number of distinct characters in the string.
    """
    return len(set(string))
