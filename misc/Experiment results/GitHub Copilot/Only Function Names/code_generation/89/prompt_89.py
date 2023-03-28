
def encrypt(s):
    """Encrypts a string using a simple algorithm.

    The algorithm is to add 1 to the ASCII value of each character.

    Args:
        s: The string to encrypt.

    Returns:
        The encrypted string.
    """
    result = ''
    for c in s:
        result += chr(ord(c) + 1)
    return result