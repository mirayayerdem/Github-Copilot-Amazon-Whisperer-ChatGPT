

def median(l: list):
    """Return the median of a list of numbers.

    >>> median([1, 2, 3])
    2
    >>> median([1, 2, 3, 4])
    2.5
    """
    "*** YOUR CODE HERE ***"
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]
