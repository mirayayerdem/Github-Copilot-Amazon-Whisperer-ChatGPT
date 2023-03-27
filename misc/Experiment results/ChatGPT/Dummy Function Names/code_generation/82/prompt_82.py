import math
def foo(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    foo('Hello') == True
    foo('abcdcba') == True
    foo('kittens') == True
    foo('orange') == False
    """
    length = len(string)
    if length < 2:
        return False
    for i in range(2, int(math.isqrt(length)) + 1):
        if length % i == 0:
            return False
    return True

