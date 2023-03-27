import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # find_zero uses Newton's method to find a zero point of a polynomial.
    # Newton's method is an iterative method to find a zero point of a function.
    # The method is as follows:
    # 1. Start with a guess x0
    # 2. Calculate the slope of the function at x0
    # 3. Calculate the next guess x1 = x0 - f(x0) / f'(x0)
    # 4. Repeat 2 and 3 until the guess is good enough.
    # In this case, we use the following:
    # f(x) = xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    # f'(x) = xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 + .... (n + 1) * xs[n + 1] * x^n
    # f(x) = 0
    # f'(x) = xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 + .... (n + 1) * xs[n + 1] * x^n = 0
    # x = -xs[1] / (2 * xs[2]) - 3 * xs[3] / (4 * xs[2]^2) * x^2 - .... (n + 1) * xs[n + 1] / (n + 2) * xs[2]^(n + 1) * x^n
    # x = -xs[1] / (2 * xs[2]) - 3 * xs[3] / (4 * xs[2]^2) * x^2 - .... (n + 1) * xs[n + 1] / (n + 2) * xs[2]^(n + 1) * x^n
    # x = -xs[1] / (2 * xs[2]) - 3 * xs[3] / (4 * xs[2]^2) * x^2 - .... (n + 1) * xs[n + 1] / (n + 2) * xs[2]^(n + 1)
