

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def foo(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> foo('')
    ''
    >>> foo('cat')
    'catac'
    >>> foo('cata')
    'catac'
    """
    if not string:
        return string
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string[:i] + string[i:][::-1]
    return string + string[::-1]
