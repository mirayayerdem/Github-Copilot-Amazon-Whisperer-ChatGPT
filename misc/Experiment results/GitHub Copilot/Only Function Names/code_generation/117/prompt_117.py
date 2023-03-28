
def select_words(s, n):
    """Returns a list of words in s that have length n."""
    return [word for word in s.split() if len(word) == n]
    