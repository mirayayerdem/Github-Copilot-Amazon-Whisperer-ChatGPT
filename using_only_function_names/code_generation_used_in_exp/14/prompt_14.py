from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Returns all prefixes of a string.
    :param string: String to get prefixes of.
    :return: List of prefixes.
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i + 1])
    return prefixes
