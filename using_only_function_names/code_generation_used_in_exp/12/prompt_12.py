from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Finds the longest string in a list of strings.
    :param strings: List of strings.
    :return: The longest string in the list, or None if the list is empty.
    """
    longest_string = None
    for string in strings:
        if longest_string is None or len(string) > len(longest_string):
            longest_string = string
    return longest_string

