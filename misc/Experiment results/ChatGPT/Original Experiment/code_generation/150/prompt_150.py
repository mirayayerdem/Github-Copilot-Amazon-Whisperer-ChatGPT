def x_or_y(n, x, y):
    if n < 2:
        return y
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return y
    return x