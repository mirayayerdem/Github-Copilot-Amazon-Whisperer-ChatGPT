
def foo(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    foo("yogurt") ==> "u"
    foo("FULL") ==> "U"
    foo("quick") ==> ""
    foo("ab") ==> ""
    """
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    result = ''
    for i in range(len(word)):
        if word[i] in vowels:
            if word[i-1] in consonants and word[i+1] in consonants:
                result = word[i]
                break
    return result
