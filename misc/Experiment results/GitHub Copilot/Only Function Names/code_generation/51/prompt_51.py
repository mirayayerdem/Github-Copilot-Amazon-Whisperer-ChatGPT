

def remove_vowels(text):
    """Return text with vowels removed."""
    vowels = "aeiou"
    result = ""
    for letter in text:
        if letter.lower() not in vowels:
            result += letter
    return result
