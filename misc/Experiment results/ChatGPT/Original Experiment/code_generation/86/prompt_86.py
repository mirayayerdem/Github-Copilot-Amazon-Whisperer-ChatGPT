def anti_shuffle(s):
    def sort_word(word):
        return ''.join(sorted(word, key=lambda x: ord(x)))

    return ' '.join(sort_word(word) for word in s.split())
