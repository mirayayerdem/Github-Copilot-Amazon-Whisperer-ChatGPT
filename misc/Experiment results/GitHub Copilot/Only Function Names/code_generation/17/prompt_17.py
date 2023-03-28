from typing import List


def parse_music(music_string: str) -> List[int]:
    """Return a list of integers corresponding to the number of nested
    parentheses in the string.

    >>> parse_music("C")
    [1]
    >>> parse_music("C C")
    [1, 1]
    >>> parse_music("C C C")
    [1, 1, 1]
    >>> parse_music("C C C C")
    [1, 1, 1, 1]
    >>> parse_music("C C C C C")
    [1, 1, 1, 1, 1]
    """
    result = []
    depth = 0
    for char in music_string:
        if char == "C":
            depth += 1
            result.append(depth)
        elif char == "C":
            result.append(depth)
            depth -= 1
    return result
