
def foo(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    foo(12, 15) = 14
    foo(13, 12) = -1
    """
    return max(x, y) if x % 2 == 0 and y % 2 == 0 else -1
