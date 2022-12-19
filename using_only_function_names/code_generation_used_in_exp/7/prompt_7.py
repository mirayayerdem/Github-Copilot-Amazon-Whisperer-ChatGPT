from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filters a list of strings by a substring.
    :param strings: List of strings.
    :param substring: Substring to filter by.
    :return: List of strings filtered by the substring.
    """
    filtered_strings = []
    for string in strings:
        if substring in string:
            filtered_strings.append(string)
    return filtered_strings
