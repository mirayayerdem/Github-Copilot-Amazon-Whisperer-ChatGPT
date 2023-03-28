import re

def select_words(s, n):
    # split the string into words
    words = re.findall(r'\b\w+\b', s)
    # check if the word has exactly n consonants
    result = [word for word in words if len([c for c in word if c.isalpha() and c not in "aeiouAEIOU"]) == n]
    return result
