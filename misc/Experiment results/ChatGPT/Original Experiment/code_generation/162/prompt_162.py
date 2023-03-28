import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == "":
        return None
    else:
        # create a new md5 hash object
        m = hashlib.md5()
        # update the hash object with bytes of the string
        m.update(text.encode())
        # return the hexadecimal representation of the hash
        return m.hexdigest()
