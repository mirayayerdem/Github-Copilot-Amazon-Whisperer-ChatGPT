def find_max(words):
    max_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_word = word
            max_length = len(word)
    return max_word
