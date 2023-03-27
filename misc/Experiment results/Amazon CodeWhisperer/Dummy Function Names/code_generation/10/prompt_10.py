

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
    postfix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            postfix = string[i:]
            break
    return string + postfix[::-1]
