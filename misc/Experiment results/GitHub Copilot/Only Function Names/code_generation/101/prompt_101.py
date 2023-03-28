
def words_string(s):
    """Return a string with the words in s in reverse order.

    Args:
        s: A string of words separated by spaces.

    Returns:
        A string with the words in s in reverse order.
    """
    words = s.split()
    result = ''
    for word in words:
        result = word + ' ' + result
    return result