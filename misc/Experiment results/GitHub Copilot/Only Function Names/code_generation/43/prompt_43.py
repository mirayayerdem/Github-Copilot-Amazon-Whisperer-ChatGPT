

def pairs_sum_to_zero(l):
    """Return a list of all pairs that sum to zero.

    >>> pairs_sum_to_zero([1, 2, -2, -1])
    [[1, -1], [2, -2]]
    """
    "*** YOUR CODE HERE ***"
    result = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                result.append([l[i], l[j]])
    return result
