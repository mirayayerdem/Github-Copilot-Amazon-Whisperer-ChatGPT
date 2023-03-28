import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list, epsilon=1e-6):
    def poly(x):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    a, b = -1e6, 1e6  # Initialize interval to large range around zero
    while abs(b - a) > epsilon:  # Repeat until interval is narrow enough
        mid = (a + b) / 2  # Find midpoint of interval
        if poly(a) * poly(mid) < 0:  # Zero lies in left half of interval
            b = mid
        else:  # Zero lies in right half of interval
            a = mid
    return (a + b) / 2  # Return midpoint of final interval
