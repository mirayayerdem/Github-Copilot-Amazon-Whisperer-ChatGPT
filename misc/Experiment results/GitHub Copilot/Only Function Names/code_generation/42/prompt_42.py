

def incr_list(l: list):
    """Return a list of all triples that sum to zero.

    >>> incr_list([1, 2, -2, -1])
    [[1, 2, -3], [1, -1, 0], [2, -2, 0]]
    """
    "*** YOUR CODE HERE ***"
    result = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    result.append([l[i], l[j], l[k]])
    return result
