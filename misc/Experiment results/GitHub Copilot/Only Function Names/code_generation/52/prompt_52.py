

def below_threshold(l: list, t: int):
    """Return a list of all numbers in l that are below t.

    >>> below_threshold([1, 2, 3], 2)
    [1]
    >>> below_threshold([1, 2, 3], 4)
    [1, 2, 3]
    """
    "*** YOUR CODE HERE ***"
    result = []
    for i in range(len(l)):
        if l[i] < t:
            result.append(l[i])
    return result
