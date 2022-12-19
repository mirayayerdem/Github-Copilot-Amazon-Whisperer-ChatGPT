import math


def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds the zero of a polynomial.
    :param xs: coefficients of the polynomial.
    :return: zero of the polynomial.
    """
    return -xs[-1] / xs[-2]
