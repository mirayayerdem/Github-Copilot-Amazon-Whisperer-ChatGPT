

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    if is_palindrome(string):
        return string
    else:
        for i in range(len(string)):
            if is_palindrome(string[:i] + string[i+1:]):
                return string[:i] + string[i+1:]
    return ""
