
def words_in_sentence(sentence):
    """ (str) -> list of str

    Return a list of the words in sentence.

    >>> words_in_sentence('The cat ate the rat.')
    ['The', 'cat', 'ate', 'the', 'rat.']
    """

    words = []
    word = ''

    for char in sentence:
        if char == ' ':
            words.append(word)
            word = ''
        else:
            word = word + char

    words.append(word)

    return words