
def foo(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    foo('Hi') returns 'Hi'
    foo('hello') returns 'ehllo'
    foo('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    return ' '.join(sorted(s.split(), key=lambda x: ''.join(sorted(x))))
