import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def foo(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(foo([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(foo([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # find_zero only takes list xs having even number of coefficients
    assert len(xs) % 2 == 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-1] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[0] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[1] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-2] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[2] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-3] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[3] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-4] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[4] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-5] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[5] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-6] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[6] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-7] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[7] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-8] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[8] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[-9] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs[9] != 0
    # find_zero only takes list xs having even number of coefficients
    assert xs

