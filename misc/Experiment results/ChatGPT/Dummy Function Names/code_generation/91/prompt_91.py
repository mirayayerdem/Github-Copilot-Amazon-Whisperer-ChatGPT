
def foo(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> foo("Hello world")
    0
    >>> foo("The sky is blue. The sun is shining. I love this weather")
    1
    """
    boredom_count = 0
    sentences = S.split('. ')
    for sentence in sentences:
        if sentence.startswith('I '):
            boredom_count += 1
    return boredom_count
