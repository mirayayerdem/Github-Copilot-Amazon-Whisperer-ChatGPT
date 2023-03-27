
def foo(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    foo("1/5", "5/1") = True
    foo("1/6", "2/1") = False
    foo("7/10", "10/2") = False
    """
    x = Fraction(x)
    n = Fraction(n)
    result = x * n
    if result.denominator == 1:
        return True
    return False
