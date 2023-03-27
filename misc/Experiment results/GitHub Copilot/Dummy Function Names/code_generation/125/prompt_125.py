
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
    return [i for i in txt.split() if i] if txt.count(' ') else [i for i in txt.split(',') if i] if txt.count(',') else len([i for i in txt if ord(i) % 2 == 1 and i.islower()])
