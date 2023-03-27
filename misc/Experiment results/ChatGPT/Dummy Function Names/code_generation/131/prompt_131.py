
def foo(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    foo(1)  == 1
    foo(4)  == 0
    foo(235) == 15
    """
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
        else:
            product = product
    if product == 1:
        return 0
    else:
        return product

