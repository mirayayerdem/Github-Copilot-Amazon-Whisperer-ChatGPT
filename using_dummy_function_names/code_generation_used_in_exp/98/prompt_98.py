
def foo(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    foo('aBCdEf') returns 1
    foo('abcdefg') returns 0
    foo('dBBE') returns 0
    """
    return sum(1 for i in range(len(s)) if i % 2 == 0 and s[i].upper() in 'AEIOU')
