

def how_many_times(string: str, substring: str) -> int:
    """Return the number of times substring appears in string.
    
    >>> how_many_times("hello", "l")
    2
    >>> how_many_times("hello", "o")
    1
    >>> how_many_times("hello", "x")
    0
    >>> how_many_times("hello", "hello")
    1
    >>> how_many_times("hello", "hello world")
    0
    """
    # BEGIN PROBLEM 18
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
    # END PROBLEM 18