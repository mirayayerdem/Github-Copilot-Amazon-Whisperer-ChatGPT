

def foo(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> foo([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> foo([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return [0]
    return [xs[i] * i for i in range(1, len(xs))]
