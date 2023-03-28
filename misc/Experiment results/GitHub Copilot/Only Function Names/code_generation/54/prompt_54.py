

def same_chars(s0: str, s1: str):
    """Return True if s0 and s1 have the same characters, False otherwise.
    """
    "*** YOUR CODE HERE ***"
    if len(s0) != len(s1):
        return False
    for i in range(len(s0)):
        if s0[i] not in s1:
            return False
    return True
