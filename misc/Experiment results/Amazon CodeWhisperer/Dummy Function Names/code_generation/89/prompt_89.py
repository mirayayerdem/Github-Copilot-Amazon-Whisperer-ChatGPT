
def foo(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    foo('hi') returns 'lm'
    foo('asdfghjkl') returns 'ewhjklnop'
    foo('gf') returns 'kj'
    foo('et') returns 'ix'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([alphabet[(alphabet.index(c) + 2) % 26] for c in s])
