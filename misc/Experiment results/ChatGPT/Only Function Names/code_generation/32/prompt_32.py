import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    left = -100
    right = 100
    while abs(right - left) > 1e-10:
        middle = (left + right) / 2
        if poly(xs, middle) < 0:
            left = middle
        else:
            right = middle
    return (left + right) / 2
