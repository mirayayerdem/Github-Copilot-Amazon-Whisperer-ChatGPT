

def remove_vowels(text):
    """
    Remove vowels from a string.
    :param text: string
    :return: string
    """
    vowels = "aeiouAEIOU"
    new_text = ""
    for char in text:
        if char not in vowels:
            new_text += char
    return new_text
