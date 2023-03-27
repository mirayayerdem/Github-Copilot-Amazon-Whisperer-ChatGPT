

def encode_shift(s: str):
    """
    Encode a string using the shift cipher.

    :param s: The string to encode.
    :return: The encoded string.
    """
    return ''.join([chr(ord(c) + 1) for c in s])
