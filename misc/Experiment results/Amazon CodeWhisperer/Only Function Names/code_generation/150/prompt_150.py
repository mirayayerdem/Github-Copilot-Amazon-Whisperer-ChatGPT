
def x_or_y(n, x, y):
    if n == 1:
        return x
    if n == 2:
        return y
    return x_or_y(n-1, x, y) + x_or_y(n-2, x, y)

