

def monotonic(l: list):
    """Return True if the list is monotonic.

    >>> monotonic([1, 2, 3])
    True
    >>> monotonic([1, 2, 1])
    False
    """
    "*** YOUR CODE HERE ***"
    if len(l) <= 2:
        return True
    else:
        if l[0] < l[1]:
            for i in range(1, len(l) - 1):
                if l[i] > l[i+1]:
                    return False
            return True
        elif l[0] > l[1]:
            for i in range(1, len(l) - 1):
                if l[i] < l[i+1]:
                    return False
            return True
        else:
            return monotonic(l[1:])
