def remove_vowels(text):
    return "".join([ch for ch in text if ch.lower() not in "aeiou"])
