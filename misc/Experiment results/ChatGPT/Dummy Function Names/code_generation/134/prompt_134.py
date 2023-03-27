
import re
def foo(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    foo("apple pie") ➞ False
    foo("apple pi e") ➞ True
    foo("apple pi e ") ➞ False
    foo("") ➞ False 
    '''
    if txt == "":
        return False
    elif re.search("[a-zA-Z]\s$", txt):
        return True
    else:
        return False
