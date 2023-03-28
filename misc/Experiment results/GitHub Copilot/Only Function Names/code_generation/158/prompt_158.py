
def find_max(words):
    """ (list of str) -> str

    Return the longest string in words.

    Precondition: words has at least one item.

    >>> find_max(['cat', 'dog', 'mouse'])
    'mouse'
    >>> find_max(['cat', 'dog', 'mouse', 'elephant'])
    'elephant'
    """
    max_len = 0
    max_word = ''

    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            max_word = word

    return max_word