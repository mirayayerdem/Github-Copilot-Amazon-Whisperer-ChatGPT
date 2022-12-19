

def foo(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> foo('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> foo('abcd', 'dddddddabc')
    True
    >>> foo('dddddddabc', 'abcd')
    True
    >>> foo('eabcd', 'dddddddabc')
    False
    >>> foo('abcd', 'dddddddabce')
    False
    >>> foo('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return len(s0) == len(s1) and all(c in s1 for c in s0)
