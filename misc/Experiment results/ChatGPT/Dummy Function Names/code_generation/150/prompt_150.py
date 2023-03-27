
def foo(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for foo(7, 34, 12) == 34
    for foo(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
