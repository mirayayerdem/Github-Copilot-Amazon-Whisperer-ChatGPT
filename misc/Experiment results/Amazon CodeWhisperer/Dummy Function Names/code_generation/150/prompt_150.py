
def foo(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for foo(7, 34, 12) == 34
    for foo(15, 8, 5) == 5

    """
    if n == 1:
        return x
    else:
        return y
