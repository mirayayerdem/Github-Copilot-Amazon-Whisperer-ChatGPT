
def foo(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    foo('aBCdEf') returns 1
    foo('abcdefg') returns 0
    foo('dBBE') returns 0
    """
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOUaeiou':
            count += 1
    return count
