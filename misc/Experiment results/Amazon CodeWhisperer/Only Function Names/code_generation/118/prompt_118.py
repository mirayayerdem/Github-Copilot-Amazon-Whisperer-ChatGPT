
def get_closest_vowel(word):
    '''
    word: a string
    returns: the closest vowel to the end of word
    '''
    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            return word[i]
    return 'a'

