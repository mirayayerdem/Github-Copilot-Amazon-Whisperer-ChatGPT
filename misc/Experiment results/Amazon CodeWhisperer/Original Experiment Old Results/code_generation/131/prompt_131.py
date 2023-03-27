
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # your code here
    if n == 0:
        return 0
    if n % 2 == 0:
        return digits(n // 10)
    else:
        return digits(n // 10) * (n % 10)
