
def get_closest_vowel(word):
    """
    Returns the closest vowel to the first vowel in a word.
    :param word: Word.
    :return: Closest vowel to the first vowel in a word.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    first_vowel = word[0]
    if first_vowel in vowels:
        return first_vowel
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i]


