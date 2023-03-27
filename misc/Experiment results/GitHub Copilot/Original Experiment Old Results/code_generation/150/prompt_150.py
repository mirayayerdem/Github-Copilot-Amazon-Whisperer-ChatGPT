
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    return x if is_prime(n) else y


def is_prime(n):
    """
    Given a number n, return True if it is prime, and False otherwise.
    Example:
        is_prime(1) ➞ False
        is_prime(2) ➞ True
        is_prime(3) ➞ True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

    





