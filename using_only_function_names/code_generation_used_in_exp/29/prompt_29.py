from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filters a list of strings by a prefix.
    :param strings: List of strings.
    :param prefix: Prefix to filter by.
    :return: List of strings filtered by the prefix.
    """
    filtered_strings = []
    for string in strings:
        if string.startswith(prefix):
            filtered_strings.append(string)
    return filtered_strings
