
def foo(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        foo("") => 0
        foo("abAB") => 131
        foo("abcCd") => 67
        foo("helloE") => 69
        foo("woArBld") => 131
        foo("aAaaaXa") => 153
    """
    return sum(map(lambda x: ord(x.upper()), s))
