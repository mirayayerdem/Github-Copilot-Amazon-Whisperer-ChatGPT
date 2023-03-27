from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter a list of strings by a prefix.
    """
    return [s for s in strings if s.startswith(prefix)]