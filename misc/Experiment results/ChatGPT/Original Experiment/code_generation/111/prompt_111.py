import collections
def histogram(test):
    test = test.split(" ")
    letter_count = collections.Counter(test)
    max_count = max(letter_count.values())
    max_letters = {k: v for k, v in letter_count.items() if v == max_count}
    return max_letters
