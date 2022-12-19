
def foo(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for foo(7, 34, 12) == 34
    for foo(15, 8, 5) == 5
    
    """
    return x if is_prime(n) else y


def is_prime(n):
    """A simple function which should return True if n is a prime number and False otherwise.

    Examples:
    for is_prime(7) == True
    for is_prime(15) == False
    """
    return True if n > 1 and all(n % i for i in range(2, n)) else False
