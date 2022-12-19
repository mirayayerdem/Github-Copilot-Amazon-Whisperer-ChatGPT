
def foo(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    foo("Mary had a little lamb", 4) ==> ["little"]
    foo("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    foo("simple white space", 2) ==> []
    foo("Hello world", 4) ==> ["world"]
    foo("Uncle sam", 3) ==> ["Uncle"]
    """
    return [word for word in s.split() if sum(1 for c in word if c.lower() in 'aeiou') == n]
