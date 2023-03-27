from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter a list of strings by a substring.
    """
    return [s for s in strings if substring in s]
