

def count_distinct_characters(string: str) -> int:
    """
    Counts the number of distinct characters in a string.
    :param string: String to count distinct characters in.
    :return: Number of distinct characters in the string.
    """
    distinct_characters = set()
    for c in string:
        distinct_characters.add(c)
    return len(distinct_characters)
