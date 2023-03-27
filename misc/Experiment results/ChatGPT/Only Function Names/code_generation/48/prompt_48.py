

def is_palindrome(text: str):
    text = text.lower()
    return text == text[::-1]
