
def anti_shuffle(s):
    """
    >>> anti_shuffle('abcdefghijklmnopqrstuvwxyz')
    'abcdefghijklmnopqrstuvwxyz'
    >>> anti_shuffle('zyxwvutsrqponmlkjihgfedcba')
    'zyxwvutsrqponmlkjihgfedcba'
    >>> anti_shuffle('zyxwvutsrqponmlkjihgfedcba')
    'zyxwvutsrqponmlkjihgfedcba'
    >>> anti_shuffle('abcd')
    'abcd'
    >>> anti_shuffle('zyxw')
    'zyxw'
    """
    return s[::-1]

