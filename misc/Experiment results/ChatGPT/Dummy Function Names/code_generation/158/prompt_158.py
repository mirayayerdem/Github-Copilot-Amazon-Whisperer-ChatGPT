
def foo(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    foo(["name", "of", "string"]) == "string"
    foo(["name", "enam", "game"]) == "enam"
    foo(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_unique_chars = 0
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_word = word
            max_unique_chars = unique_chars
        elif unique_chars == max_unique_chars:
            if word < max_word:
                max_word = word
    return max_word
