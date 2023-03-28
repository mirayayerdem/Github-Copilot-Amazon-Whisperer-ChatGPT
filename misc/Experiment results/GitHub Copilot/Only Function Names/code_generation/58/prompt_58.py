

def common(l1: list, l2: list):
    """Return a list of all elements that appear in both l1 and l2.

    >>> common([1, 2, 3], [2, 3, 4])
    [2, 3]
    """
    "*** YOUR CODE HERE ***"
    result = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                result.append(l1[i])
    return result
