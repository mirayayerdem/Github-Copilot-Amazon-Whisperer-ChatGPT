

def is_palindrome(text: str):
    """
    Checks if a string is a palindrome.
    :param text: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    return text == text[::-1]
