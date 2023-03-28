

def derivative(xs: list):
    """Return the derivative of the function defined by xs.

    >>> derivative([(0, 1), (1, 2), (2, 3)])
    [1, 1]
    """
    "*** YOUR CODE HERE ***"
    result = []
    for i in range(len(xs) - 1):
        result.append((xs[i+1][1] - xs[i][1]) / (xs[i+1][0] - xs[i][0]))
    return result
