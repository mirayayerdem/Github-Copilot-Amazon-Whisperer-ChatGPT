import math


def poly(xs: list, x: float):
    res = 0
    for i in range(len(xs)):
        res += xs[i] * (x ** i)
    return res
