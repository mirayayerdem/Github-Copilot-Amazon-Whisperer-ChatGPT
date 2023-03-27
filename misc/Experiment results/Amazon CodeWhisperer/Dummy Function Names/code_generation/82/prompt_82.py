
def foo(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    foo('Hello') == True
    foo('abcdcba') == True
    foo('kittens') == True
    foo('orange') == False
    """
    if string == '':
        return True
    else:
        for i in range(2, string):
            if string % i == 0:
                return False
        return True
