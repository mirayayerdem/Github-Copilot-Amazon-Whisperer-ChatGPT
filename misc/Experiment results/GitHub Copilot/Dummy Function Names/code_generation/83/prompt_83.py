
def foo(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2
    else:
        return 9 * 10**(n-2) + foo(n-1)
