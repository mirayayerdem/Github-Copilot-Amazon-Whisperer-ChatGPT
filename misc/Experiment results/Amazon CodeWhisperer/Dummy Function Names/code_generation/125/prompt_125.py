
def foo(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    foo("Hello world!") ➞ ["Hello", "world!"]
    foo("Hello,world!") ➞ ["Hello", "world!"]
    foo("abcdef") == 3 
    '''
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum([1 for i in txt if ord(i) % 2 == 1])
