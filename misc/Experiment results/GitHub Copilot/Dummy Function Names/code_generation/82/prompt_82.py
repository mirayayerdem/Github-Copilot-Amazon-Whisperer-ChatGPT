
def foo(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    foo('Hello') == True
    foo('abcdcba') == True
    foo('kittens') == True
    foo('orange') == False
    """
    if len(string) == 2 or len(string) == 3:
        return True
    if len(string) % 2 == 0:
        return False
    if len(string) % 3 == 0:
        return False
    i = 5
    while i * i <= len(string):
        if len(string) % i == 0:
            return False
        if len(string) % (i + 2) == 0:
            return False
        i = i + 6
    return True
