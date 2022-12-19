
def foo(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 for i in range(1, n+1) if str(i).startswith('1') or str(i).endswith('1'))
