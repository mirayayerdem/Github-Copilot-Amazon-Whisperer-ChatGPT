

def encode_cyclic(s: str):
    """
    Encodes a string by replacing each character with its ASCII code.
    """
    return ''.join(str(ord(c)) for c in s)