
import hashlib
def foo(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> foo('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == "":
        return None
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()
