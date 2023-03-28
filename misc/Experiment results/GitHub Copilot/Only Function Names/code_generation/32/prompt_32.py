import math


def poly(xs: list, x: float):
    result = 0
    for i in range(len(xs)):
        result += xs[i] * math.pow(x, i)
    return result
