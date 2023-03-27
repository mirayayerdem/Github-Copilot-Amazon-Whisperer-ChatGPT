
def foo(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    foo(1)  == 1
    foo(4)  == 0
    foo(235) == 15
    """
    if n == 0:
        return 0
    else:
        return (n % 10) * foo(n // 10)
