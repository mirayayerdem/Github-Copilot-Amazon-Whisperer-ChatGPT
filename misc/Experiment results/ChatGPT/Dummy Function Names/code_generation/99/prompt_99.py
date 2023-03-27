
def foo(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> foo("10")
    10
    >>> foo("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example foo("14.5") should
    return 15 and foo("-14.5") should return -15.
    '''
    return round(float(value))