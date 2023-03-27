

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(c for c in text if c not in vowels)
