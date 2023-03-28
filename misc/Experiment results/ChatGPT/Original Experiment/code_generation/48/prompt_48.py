def is_palindrome(text: str):
    # Return True for empty string or string of length 1
    if len(text) <= 1:
        return True
    # Compare first and last characters
    if text[0] != text[-1]:
        return False
    # Recursively check middle part of string
    return is_palindrome(text[1:-1])
