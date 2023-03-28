

def is_palindrome(text: str):
    """Return True if text is a palindrome, False otherwise."""
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[-i - 1]:
            return False
    return True
