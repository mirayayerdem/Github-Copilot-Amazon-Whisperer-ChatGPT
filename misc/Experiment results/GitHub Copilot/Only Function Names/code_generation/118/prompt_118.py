
def get_closest_vowel(word):
    """ (str) -> str

    Return the vowel in word that is closest to the beginning of word. If
    there is a tie, return the vowel that appears first. Vowels are
    'a', 'e', 'i', 'o', and 'u'. Assume word contains at least one vowel.

    >>> get_closest_vowel('apple')
    'a'
    >>> get_closest_vowel('aerial')
    'e'
    >>> get_closest_vowel('question')
    'e'
    >>> get_closest_vowel('string')
    'i'
    """

    vowels = 'aeiou'
    closest_vowel = word[0]
    for char in word:
        if char in vowels:
            if vowels.index(char) < vowels.index(closest_vowel):
                closest_vowel = char
    return closest_vowel