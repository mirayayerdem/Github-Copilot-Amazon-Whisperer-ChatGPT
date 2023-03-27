
def foo(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    foo(12, 15) = 14
    foo(13, 12) = -1
    """
    if x > y:
        return -1
    elif x % 2 == 0:
        return max(x, x + (y - x) // 2 * 2)
    else:
        return max(x + 1, x + (y - x) // 2 * 2)
