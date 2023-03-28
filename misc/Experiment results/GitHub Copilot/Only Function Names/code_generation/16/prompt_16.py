

def count_distinct_characters(string: str) -> int:
    """Return the number of distinct characters in the string.
    
    >>> count_distinct_characters("hello")
    4
    >>> count_distinct_characters("hello world")
    10
    >>> count_distinct_characters("hello world!")
    11
    >>> count_distinct_characters("")
    0
    """
    distinct_characters = set()
    for char in string:
        distinct_characters.add(char)
    return len(distinct_characters)