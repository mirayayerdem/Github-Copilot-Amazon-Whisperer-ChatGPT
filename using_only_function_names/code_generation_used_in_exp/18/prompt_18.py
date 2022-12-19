

def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a substring occurs in a string.
    :param string: String to search in.
    :param substring: Substring to search for.
    :return: Number of times the substring occurs in the string.
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count
