
def string_to_md5(text):
    """ (str) -> str

    Return the MD5 hash of the string text.

    >>> string_to_md5('hello')
    '5d41402abc4b2a76b9719d911017c592'
    """
    return hashlib.md5(text.encode()).hexdigest()