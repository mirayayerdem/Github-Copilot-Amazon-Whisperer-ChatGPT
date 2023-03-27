
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    """A simple program which should return True if n is a prime number
    and False otherwise.

    Examples:
    for is_prime(7) == True
    for is_prime(15) == False
    
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True