
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
    vowels = "aeiouAEIOU"
    word = word[::-1]
    for i, c in enumerate(word):
        if c in vowels:
            if i+1 < len(word) and i-1 >= 0:
                if word[i+1] not in vowels and word[i-1] not in vowels:
                    return c
    return ""
