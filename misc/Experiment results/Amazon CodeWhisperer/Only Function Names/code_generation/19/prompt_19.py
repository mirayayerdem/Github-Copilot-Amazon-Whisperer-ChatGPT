from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Sort numbers in a string.
    """
    return " ".join(sorted(numbers.split(), key=int))
