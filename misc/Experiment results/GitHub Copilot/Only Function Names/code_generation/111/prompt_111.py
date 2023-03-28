
def histogram(test):
    
    """ (list of number) -> list of number

    Return a list of numbers that represents the histogram of the given list.

    >>> histogram([1, 2, 3])
    [1, 2, 3]
    >>> histogram([1, 1, 1])
    [3]
    >>> histogram([1, 2, 1, 2, 1, 2])
    [3, 3]

    """
    result = []
    for i in range(len(test)):
        if test[i] not in result:
            result.append(test[i])
    for i in range(len(result)):
        result[i] = test.count(result[i])
    return result