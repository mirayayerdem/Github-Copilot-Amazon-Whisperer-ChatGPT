

def string_sequence(n: int) -> str:
    """
    Returns a string of the form "aabbbccdddd"
    """
    result = ""
    for i in range(n):
        result += chr(97 + i) * (i + 1)
    return result